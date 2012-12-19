# -*- coding: utf-8 -*-

from django.template import Context, loader
from django.http import HttpResponse

import datetime

def hello(request):
    return HttpResponse("Hello, world.")


def index(request):
    t = loader.get_template('tmpl/index.html')
    d = datetime.datetime.now()
    PUB_DATE = d.strftime("%d/%m/%Y %X")

    c = Context({ 
        'DATA': "TEST DE DATA", 
        'PUB_DATE':PUB_DATE, 
        'TITRE_PAGE' : 'WELCOME',
        })
    return HttpResponse(t.render(c))

def menu(request):
    TITRE_PAGE = "MENU PRINCIPAL"
    t = loader.get_template('tmpl/menu.html')

    d = datetime.datetime.now()
    PUB_DATE = d.strftime("%d/%m/%Y %X")

    menu = [
        ('fex/' , 'Gestions des Echanges de fichiers'),
        ('put_file' , 'Déposer un fichier'),
        ('get_file' , 'Récuperer un fichier'),
        ('param' , 'Paramètre Généraux'),
    ]

    c = Context({ 
        'PUB_DATE':PUB_DATE, 
        'TITRE_PAGE' : TITRE_PAGE,
        'menu_items' : menu
        })
    return HttpResponse(t.render(c))

def put_file(request):
    return HttpResponse("NON IMPLEMENTEE : put_file")

def get_file(request):
    return HttpResponse("NON IMPLEMENTEE : get_file")

def param(request):
    return HttpResponse("NON IMPLEMENTEE : param")
