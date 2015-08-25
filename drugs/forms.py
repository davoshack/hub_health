# -*- coding: utf-8 -*-
import os, sys

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import Drugs
from django.forms import Textarea, TextInput, FileInput, DateInput, RadioSelect, NumberInput

class DrugsForm(forms.ModelForm):
    class Meta:
        model = Drugs
        exclude = ('user','docis','docis_type','administration_mode','administration_cause',)
                
        widgets = {
            'name': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:90%','placeholder': _("ej: albuterol")}),
            'concentration': NumberInput(attrs={'class': 'form-control','style':'width:50%','placeholder': _("ej: 500")}),
            'concentration_type':forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'docis': NumberInput(attrs={'class': 'form-control','style':'width:30%','placeholder': _("ej: 2")}),
            'docis_type': forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'periodicity_administration': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:90%','placeholder': _("ej: 2 veces al dia")}),
            'administration_mode':forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'administration_cause': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:90%'}),
            'date_init': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerinit','style':'width:50%'}),
            'date_final': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerfinal','style':'width:50%'}),
            'note': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:98%'}),
            
        }