# -*- coding: utf-8 -*-

from django.db import models
from django import forms

from django.utils.translation import ugettext_lazy as _

# Create your models here.
TYPE_ENT = (
    ( 'ROOT' , 'ROOT' ),
    ( 'TIERS', 'TIERS'),
)


class tstClass(models.Model):
    codent = models.CharField(_(u'Code Entite'),max_length=20, unique=True)
    noment = models.CharField(_(u'Nom Entite'),max_length=40)
    description = models.TextField(_(u'Description'))
    typent = models.CharField(_(u'Type Entite'), max_length=10, choices=TYPE_ENT, default='TIERS' )

    def __unicode__(self):
        return "%s : %s" % (self.codent, self.noment)

class tstForm(forms.ModelForm):
    codent = forms.CharField(label='Code Entité ',max_length=20)
    noment = forms.CharField(label='Nom Entité ',max_length=40)
    description = forms.CharField(label='Description ', widget=forms.Textarea, required=False)
    typent = forms.ChoiceField( label='Type Entité ',choices=TYPE_ENT, initial='TIERS')
    class Meta:
        model = tstClass
