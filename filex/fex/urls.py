# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from models import UtilisateurClass

urlpatterns = patterns('fex.views',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

    # fex => Entite
    url(r'^$', 'fex_liste', name='ges_fex' ),
    url(r'^cr$', 'fex_create', name='fex_create' ),
    url(r'^(?P<fex_id>\d+)/$', 'fex_detail', name='fex_detail' ),

    # fex => User
    url(r'^usr/$', 'fex_usr_liste', name='fex_ls_usr' ),
    url(r'^liste/$', 'fex_std_liste', { 'model':UtilisateurClass, 'template':'tmpl/fex/list_usr.html', 'p':2,  }),
    )
