# -*- coding: utf-8 -*-
# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from models import EntiteClass

import datetime

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
    e = get_list_or_404(EntiteClass, typent='TIERS')

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
