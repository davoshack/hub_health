# -*- coding: utf-8 -*-
import os, sys

from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import Hemoglobin
from django.forms import Textarea, NumberInput

class HemoglobinForm(forms.ModelForm):
    class Meta:
        model = Hemoglobin
        exclude = ('user',)
                
        widgets = {
            'percent': NumberInput(attrs={'class': 'form-control','placeholder': _("%"),'style':'width:50%'}),
            'note': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:100%'}),
        }