# -*- coding: utf-8 -*-
import os, sys

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import Glycemia
from django.forms import Textarea, TextInput, FileInput, DateInput, RadioSelect, NumberInput


class GlycemiaForm(forms.ModelForm):
    class Meta:
        model = Glycemia
        exclude = ('user',)
                
        widgets = {
            'measurement': NumberInput(attrs={'class': 'form-control','placeholder': _("mg/dl"),'style':'width:50%'}),
            'measurement_context': forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'blood_type': forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'note': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:100%'}),   
        }
      