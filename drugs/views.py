# -*- encoding: utf-8 -*-
import os, sys

from django.views.generic import TemplateView,FormView
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest
from django.core.context_processors import csrf
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import *
from django.views.generic.edit import *
from django.views.generic import *
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.contrib import messages

class AddDrugs(CreateView):
    template_name = 'edit_drugs.html'
    form_class = DrugsForm
 
    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Medicamento guardado con éxito!")
    	return super(AddDrugs,self).form_valid(form)
    success_url = reverse_lazy('utilities_drugs')
    

     
class ListDrugs(ListView):
    template_name = 'drugs.html'
    form_class = DrugsForm

    success_url = reverse_lazy('utilities_drugs')
    
    def get_queryset(self):
        return Drugs.objects.order_by('-id').filter(user_id = self.request.user)
    
class UpdateDrugs(UpdateView):
    template_name = 'edit_drugs.html'
    form_class = DrugsForm
    model = Drugs

    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Medicamento actualizado con éxito!")
    	return super(UpdateDrugs,self).form_valid(form)
    success_url = reverse_lazy('utilities_drugs')
    
class DeleteDrugs(DeleteView):
    template_name = 'delete_drugs.html'
    model = Drugs

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.delete()
       messages.success(request, u"¡Medicamento eliminado con éxito!")
       return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('utilities_drugs')