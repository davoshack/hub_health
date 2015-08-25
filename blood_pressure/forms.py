# -*- coding: utf-8 -*-
import os, sys

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import Pressure
from django.forms import Textarea, TextInput, FileInput, DateInput, RadioSelect, NumberInput


class PressureForm(forms.ModelForm):
    class Meta:
        model = Pressure
        exclude = ('user',)
        
        widgets = {
            'systolic': NumberInput(attrs={'class': 'form-control','placeholder': _("mmHg"),'style':'width:50%'}),
            'diastolic': NumberInput(attrs={'class': 'form-control','placeholder': _("mmHg"),'style':'width:50%'}),     
            'bpm': NumberInput(attrs={'class': 'form-control','style':'width:50%'}),
            'beat_status':forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'note': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:100%'}),
        }           