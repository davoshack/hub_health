# -*- coding: utf-8 -*-
from django import forms


class SearchDirectoryForm(forms.Form):

    first_name = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))