# -*- coding: utf-8 -*-
# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

from models import EntiteClass
from models import EntiteForm

from django import forms

import datetime
import pdb

def test_fex_liste(request):
    return HttpResponse("NON IMPLEMENTEE : ges_fex => liste ")

def test_fex_detail(request, fex_id):
    return HttpResponse("NON IMPLEMENTEE : fex_detail => %s" % fex_id)

def fex_liste(request):
    TITRE_PAGE = "FLEX EXCHANGE DETAIL / LISTE"
    t = loader.get_template('tmpl/fex/liste.html')

    d = datetime.datetime.now()
    PUB_DATE = d.strftime("%d/%m/%Y %X")
    e = EntiteClass.objects.all()
    #e = get_list_or_404(EntiteClass, typent='TIERS')

    c = Context({ 
        'PUB_DATE':PUB_DATE, 
        'TITRE_PAGE' : TITRE_PAGE,
        'all_e' : e,
        })
    return HttpResponse(t.render(c))

def fex_detail(request, fex_id):
    TITRE_PAGE = "FLEX EXCHANGE DETAIL"
    t = loader.get_template('tmpl/fex/detail.html')

    d = datetime.datetime.now()
    PUB_DATE = d.strftime("%d/%m/%Y %X")
    #e = get_object_or_404(EntiteClass, pk=fex_id)
    e = EntiteClass.objects.get(id=fex_id)

    c = Context({ 
        'PUB_DATE':PUB_DATE, 
        'TITRE_PAGE' : TITRE_PAGE,
        'entite' : e,
        })
    return HttpResponse(t.render(c))

def fex_create(request):
    if request.method == 'POST':
        ## Bouton VALID
        if request.POST['VALID'] == 'VALID':
            #pdb.set_trace()
            f = EntiteForm(request.POST)
            if f.is_valid():
                new_ent = EntiteClass()
                ## 
                new_codent = f.cleaned_data['codent']
                q = EntiteClass.objects.get(codent=new_codent)
                if q:
                    f.errors['__all__'] = f.error_class(["Cle Deja Existante"])
                else:
                    new_ent.noment = f.cleaned_data['noment']
                    new_ent.description = f.cleaned_data['description']
                    new_ent.typent = f.cleaned_data['typent']
                    new_ent.save()
                    return HttpResponseRedirect('/fex')

        else:
            ## Bouton ANNUL
            return HttpResponseRedirect('/fex')
    else:
        f = EntiteForm()

    return render( request, 'tmpl/fex/fex_create.html', { 'form' : f } )
