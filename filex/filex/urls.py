from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'filex.views.home', name='home'),
    # url(r'^filex/', include('filex.foo.urls')),

    # Home
    url(r'^$', 'filex.views.index', name='home' ),

    # Login
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'tmpl/login.html'}),

    # Menu
    url(r'^menu$', 'filex.views.menu', name='menu' ),

    # Autre fonctions
    url(r'^param$', 'filex.views.param', name='param' ),
    url(r'^put_file$', 'filex.views.put_file', name='put_file' ),
    url(r'^get_file$', 'filex.views.get_file', name='get_file' ),

    ## Gestion des fichiers Ex
    url(r'^fex/', include('fex.urls')),
    #url(r'^fex/(?P<fex_id>\d+)/$', 'fex.views.fex_detail', name='fex_detail' ),
    ## TEST
    url(r'^tst/', include('tst.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
