# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from django.views.generic import CreateView

from django.utils.translation import ugettext_lazy as _

# Create your models here.
TYPE_ENT = (
    ( 'ROOT' , 'ROOT' ),
    ( 'TIERS', 'TIERS'),
)


class EntiteClass(models.Model):
    codent = models.CharField(_(u'Code Entite'),max_length=20, unique=True)
    noment = models.CharField(_(u'Nom Entite'),max_length=40)
    description = models.TextField(_(u'Description'))
    typent = models.CharField(_(u'Type Entite'), max_length=10, choices=TYPE_ENT )

    def __unicode__(self):
        return "%s : %s" % (self.codent, self.noment)

class EntiteForm(forms.Form):
    codent = forms.CharField(label='Code Entité ',max_length=20)
    noment = forms.CharField(label='Nom Entité ',max_length=40)
    description = forms.CharField(label='Description ', widget=forms.Textarea)
    typent = forms.ChoiceField( label='Type Entité ',choices=TYPE_ENT)

class EntCreateView(CreateView):
    form_class = EntiteForm
    template_name = 'fex/Entite_new.html'
    success_url = '/fex'
