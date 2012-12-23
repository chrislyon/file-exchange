# -*- coding: utf-8 -*-
# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from models import EntiteClass
from models import EntiteForm

from models import UtilisateurClass
from models import UtilisateurForm

from django import forms

import datetime
import pdb

def get_pub_date():
    d = datetime.datetime.now()
    return d.strftime("%d/%m/%Y %X")

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

    return render( request, 'tmpl/fex/fex_create.html', { 'form' : f, 'PUB_DATE':get_pub_date() } )

def fex_usr_liste(request):
    obj_list = UtilisateurClass.objects.all()
    paginator = Paginator(obj_list, 10)

    page = request.GET.get('page')
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objs = paginator.page(paginator.num_pages)

    return render_to_response('tmpl/fex/list_usr.html', {"objs": objs})

## --------------------------------
## Liste Standard avec pagination
## --------------------------------
def fex_std_liste(request, model, template, p=10):
    d = datetime.datetime.now()
    PUB_DATE = d.strftime("%d/%m/%Y %X")

    obj_list = model.objects.all()
    paginator = Paginator(obj_list, p)

    page = request.GET.get('page')
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objs = paginator.page(paginator.num_pages)

    return render_to_response(template, {"objs": objs, 'PUB_DATE':PUB_DATE })

