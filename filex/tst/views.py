# -*- coding: utf-8 -*-
# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from models import tstClass
from models import tstForm

import datetime
import pdb

def get_pub_date():
    d = datetime.datetime.now()
    return d.strftime("%d/%m/%Y %X")

## --------------------------------
## Effacement avec ClassBase View
## --------------------------------
class URLDelete(DeleteView):
    model = tstClass
    context_object_name = "obj"
    template_name = 'tmpl/tst/tst_delete.html'
    #success_url = reverse_lazy('tst/')
    success_url = '/tst/'

    def get_object(self, queryset=None):
        enreg_id = self.kwargs.get('code', None)
        return get_object_or_404(tstClass, id=enreg_id)

## -----------------
## Modif d'un enreg
## -----------------
def tst_modif(request, enreg_id):
    if request.method == 'POST':
        if request.POST['VALID'] == 'VALID':
            a = tstClass.objects.get(id=enreg_id)
            f = tstForm(request.POST, instance=a)
            if f.is_valid():
                f.save()
                return HttpResponseRedirect('/tst')
        else:
            ## Bouton ANNUL
            return HttpResponseRedirect('/tst')
    else:
        a = tstClass.objects.get(pk=enreg_id)
        f = tstForm(instance=a)

    return render( request, 'tmpl/tst/tst_modif.html', { 'form' : f, 'ENREG':enreg_id, 'PUB_DATE':get_pub_date() } )

## -----------------------
## Creation d'un enreg
## -----------------------
def tst_create(request):
    if request.method == 'POST':
        ## Bouton VALID
        if request.POST['VALID'] == 'VALID':
            #pdb.set_trace()
            f = tstForm(request.POST)
            if f.is_valid():
                new_cle = f.cleaned_data['codent']
                try:
                    q = tstClass.objects.get(codent=new_cle)
                except:
                    q = None
                if q:
                    f.errors['__all__'] = f.error_class(["Cle Deja Existante"])
                else:
                    new_enreg = tstClass()
                    new_enreg.codent = f.cleaned_data['codent']
                    new_enreg.noment = f.cleaned_data['noment']
                    new_enreg.description = f.cleaned_data['description']
                    new_enreg.typent = f.cleaned_data['typent']
                    new_enreg.save()
                    return HttpResponseRedirect('/tst')
        else:
            ## Bouton ANNUL
            return HttpResponseRedirect('/tst')
    else:
        f = tstForm()

    return render( request, 'tmpl/tst/tst_create.html', { 'form' : f, 'PUB_DATE':get_pub_date() } )

## --------------------------------
## Liste Standard avec pagination
## --------------------------------
def std_liste(request, model, template, base_href, p=10):

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

    return render_to_response(template, {"objs": objs, 'B_HREF':base_href, 'PUB_DATE':get_pub_date() })

