# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from models import tstClass

from views import URLDelete

urlpatterns = patterns('tst.views',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

    ## model : le modele de donnees
    ## template : le template a utiliser
    ## base_href : la base pour les actions de modif delete
    ## p : le nombre d'object par pagination
    url(r'^$', 'std_liste', { 'model':tstClass, 'template':'tmpl/tst/list_tst.html', 'base_href':'/tst', 'p':10,  }, name='url_liste'),
    url(r'^liste/$', 'std_liste', { 'model':tstClass, 'template':'tmpl/tst/list_tst.html', 'base_href':'/tst', 'p':10,  }, name='url_liste'),
    ## Creation
    url(r'^create/$', 'tst_create', name='tst_create'),
    ## Modif
    url(r'^modif/(\d+)$', 'tst_modif', name='tst_modif'),
    ## Delete
    url(r'^delete/(?P<code>\d+)/$', URLDelete.as_view(), name='url_delete'),
    )
