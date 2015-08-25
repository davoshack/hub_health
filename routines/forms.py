# -*- coding: utf-8 -*-
import os, sys

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .models import ExerciseRoutines, FoodRoutines
from django.forms import Textarea, TextInput, FileInput, DateInput, RadioSelect, NumberInput

class ExerciseRoutinesForm(forms.ModelForm):
    class Meta:
        model = ExerciseRoutines
        exclude = ('user',)
        
        widgets = {
            'name': TextInput(attrs={'maxlength': 50, 'class': 'form-control','placeholder': _("ej: ciclismo"),'style':'width:50%'}),
            'description': Textarea(attrs={'cols': 10, 'rows': 3,'class': 'form-control','placeholder': _("ej: entrenamiento para partida de tenis"),'style':'width:60%'}),
            'duration': NumberInput(attrs={'class': 'form-control','placeholder': _("minutos"),'style':'width:60%'}),
            'distance': NumberInput(attrs={'class': 'form-control','placeholder': _("km"),'style':'width:60%'}),
            'steps_number': NumberInput(attrs={'class': 'form-control','style':'width:60%'}),
            'calories_burned': NumberInput(attrs={'class': 'form-control','style':'width:60%'}),
            #'fecha': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:200px'}),     
            #'hora': TextInput(attrs={'size': 6, 'class': 'form-control','maxlength': 3,'style':'width:130px','placeholder': _("ej: 11:40")}),
            'nota': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:60%'}),
            
        }
        
class FoodRoutinesForm(forms.ModelForm):
    class Meta:
        model = FoodRoutines
        exclude = ('user',)
                
        widgets = {
            'name': TextInput(attrs={'maxlength': 50, 'class': 'form-control','style':'width:90%'}),
            'food_type':forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'portion_size': NumberInput(attrs={'class': 'form-control','style':'width:50%'}),
            'amount_portion': NumberInput(attrs={'class': 'form-control','placeholder': _("ej: 2"),'style':'width:50%'}),
            'calories': NumberInput(attrs={'class': 'form-control','style':'width:50%'}),
            'date_init': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerinit','style':'width:50%'}),
            'date_final': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerfinal','style':'width:50%'}),
            'note': Textarea(attrs={'cols': 50, 'rows': 5,'class': 'form-control','style':'width:98%'}),
            
        }