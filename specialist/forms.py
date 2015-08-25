# -*- coding: utf-8 -*-
import os, sys

from django import forms
from .models import *
from django.forms import Textarea, TextInput, FileInput, DateInput
from django.utils.translation import ugettext_lazy as _
from zinnia.models.entry import Entry


class AcademicProfileForm(forms.ModelForm):
    class Meta:
        model = AcademicProfile
        exclude = ('user',)
                
        widgets = {
            'institution': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: Universidad del rosario...")}),
            'degree': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: Cirujano...")}),
            'achievements': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:100%','placeholder': _(u"ej: Becado con honores...")}),
            'date_init': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerinit','style':'width:50%'}),
            'date_final': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerfinal','style':'width:50%'}),
        }


class ProfessionalProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessionalProfile
        exclude = ('user',)
                
        widgets = {
            'organization': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: Centro de salud Las Vegas...")}),
            'position': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: Director...")}), 
            'function': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:100%','placeholder': _(u"ej: Coordinar el grupo de médicos...")}),
            'date_init': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerinit','style':'width:50%'}),
            'date_final': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerfinal','style':'width:50%'}), 
            'location': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: Av 53 S 51-3...")}),
            
        }


class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        exclude = ('user',)
                
        widgets = {
            'location': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: Av 53 S 51-3...")}),
            'phone': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%'}),
            'email': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: info@saludlasvegas.com")}),
            'mobile': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%'}),
            'institution': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%','placeholder': _(u"ej: Clínica...")}),
            'image': FileInput(attrs={'maxlength': 50, 'style':'width:60%'}),    
        }


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title','content','image','categories','authors','sites','slug','tags')
        exclude = ('user',)

        widgets = {
            'title': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:50%'}),
            'content': Textarea(attrs={'cols': 50, 'rows': 10,'class': 'form-control','style':'width:90%'}),
            'image': FileInput(attrs={'maxlength': 50, 'style':'width:40%'}),
            'categories': forms.SelectMultiple(attrs={'maxlength': 50,'class': 'form-control', 'style':'width:20%'}),
            'sites': forms.SelectMultiple(attrs={'maxlength': 50,'class': 'form-control', 'style':'width:20%'}),
            'tags': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:90%'}),
            'slug': TextInput(attrs={'maxlength': 255, 'class': 'form-control','style':'width:90%'}),
       }








