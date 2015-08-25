# -*- coding: utf-8 -*-
import os, sys

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import EmotionalStatesPatient
from django.forms import Textarea, TextInput, FileInput, DateInput, RadioSelect, NumberInput

        
class EmotionalStatesForm(forms.ModelForm):
    class Meta:
        model = EmotionalStatesPatient
        fields = ('state','note')
        
        widgets = {
            'state' : TextInput(attrs={'class': 'form-control', 'id':'state','style':'width:30%'}),
            'note': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:100%'}),
        }
        
