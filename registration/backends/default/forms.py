from django import forms
from django.utils.translation import ugettext_lazy as _
from data_users.models import ProfileUser
from django.forms import FileInput, DateInput


class PreRegisterForm(forms.Form):
    """
    Formulario de preregistro para los especialistas
    """
    email = forms.EmailField(label="Correo",max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': _("Ingresa un correo")}))
    first_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellidos",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    profession = forms.CharField(label="Profesion",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': _("ej. Pediatra")}))


class ProfileSettingForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('date_birth','sex','image')
        
        widgets = {
          
            'date_birth': DateInput(format='%d/%m/%Y',attrs={'class': 'form-control', 'id':'datePicker','style':'width:25%'}),
            'sex': forms.Select(attrs={'class':'form-control','style':'width:30%'}),
            'image': FileInput(attrs={'class': 'form-control','maxlength': 50, 'style':'width:90%'}),
            
        }    