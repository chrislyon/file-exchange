# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('fex.views',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

    # 
    url(r'^$', 'fex_liste', name='ges_fex' ),
    url(r'^(?P<fex_id>\d+)/$', 'fex_detail', name='fex_detail' ),
)
