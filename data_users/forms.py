# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import ProfileUser
from django.forms import Textarea, TextInput, FileInput, DateInput, RadioSelect, NumberInput, CheckboxInput


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = (
                  'medical_specialty',
                  'medical_emphasis',
                  'professional_abstract',
                  'patient_abstract',
                  'blood_group',
                  'sex',
                  'nationality',
                  'whatsapp',
                  'date_birth',
                  'country',
                  'city',
                  'image',
                  'professional_register',
                  'blog',
                  'twitter',
                  'facebook',
                  'linkedin',
                  'you_tube',
                  'google_plus',
                  'instagram'
                  )

        widgets = {


            'medical_specialty': forms.Select(attrs={'class':'form-control','style':'width:50%'}),
            'medical_emphasis': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:50%','placeholder': _(u"ej: educación")}),
            'professional_abstract':Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:100%','placeholder': _(u"escribe aquí un resumen de tu experiencia profesional")}),
            'patient_abstract': Textarea(attrs={'cols': 50, 'rows': 6,'class': 'form-control','style':'width:100%','placeholder': _(u"escribe aquí un resumen de tu historial médico")}),
            'blood_group': forms.Select(attrs={'class':'form-control','style':'width:30%'}),
            'sex': forms.Select(attrs={'class':'form-control','style':'width:30%'}),
            'nationality': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:30%'}),
            'date_birth': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePickerinit','style':'width:50%'}),
            'whatsapp': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:60%'}),
            'country': forms.Select(attrs={'style':'width:60%'}),
            'city': forms.Select(attrs={'style':'width:60%'}),
            'image': FileInput(attrs={'maxlength': 50, 'style':'width:90%'}),
            'professional_register': TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:48%'}),
            'blog' : TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:57%','placeholder': _(u"tublog.com")}),
            'twitter' : TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:57%','placeholder': _(u"twitter.com/tucuenta")}),
            'facebook' : TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:57%','placeholder': _(u"facebook.com/tucuenta")}),
            'linkedin' : TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:57%','placeholder': _(u"linkedin.com/tucuenta")}),
            'you_tube' : TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:57%','placeholder': _(u"youtube.com/tucuenta")}),
            'google_plus' : TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:57%','placeholder': _("")}),
            'instagram' : TextInput(attrs={'maxlength': 125, 'class': 'form-control','style':'width:57%','placeholder': _("")}),

        }


class MedicalConsultationForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('medical_consultation', 'flag_blood', 'flag_date_birth', 'flag_patient_abstract', 'flag_nationality', 'flag_message')

        widgets = {
                    'medical_consultation': CheckboxInput(attrs={'class': 'form-control'}),
                    'flag_blood': CheckboxInput(attrs={'class': 'form-control'}),
                    'flag_date_birt': CheckboxInput(attrs={'class': 'form-control'}),
                    'flag_patient_abstract': CheckboxInput(attrs={'class': 'form-control'}),
                    'flag_nationality': CheckboxInput(attrs={'class': 'form-control'}),
                    'flag_message': CheckboxInput(attrs={'class': 'form-control'}),

                  }
