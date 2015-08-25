
# -*- coding: utf-8 -*-
import os, sys

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import ClinicalSummary
from django.forms import Textarea, TextInput, FileInput, DateInput, RadioSelect, NumberInput



class ClinicalSummaryForm(forms.ModelForm):
    class Meta:
        model = ClinicalSummary
        fields = ('summary',)
                
        widgets = {
            'summary': Textarea(attrs={'cols': 70, 'rows': 15,'class': 'form-control','style':'width:90%'}),
        }
        
       