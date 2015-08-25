# -*- coding: utf-8 -*-
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

class AddHemoglobin(CreateView):

    template_name = 'edit_hemoglobin.html'
    form_class = HemoglobinForm
 
    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Información guardada con éxito!")
    	return super(AddHemoglobin,self).form_valid(form)

    success_url = reverse_lazy('account_hemoglobin')

     
class ListHemoglobin(ListView):

    template_name = 'hemoglobin.html'
    form_class = HemoglobinForm

    success_url = reverse_lazy('account_hemoglobin')
    
    def get_queryset(self):
        return Hemoglobin.objects.order_by('-id').filter(user_id = self.request.user)

    
class UpdateHemoglobin(UpdateView):

    template_name = 'edit_hemoglobin.html'
    form_class = HemoglobinForm
    model = Hemoglobin

    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Información actualizada con éxito!")
    	return super(UpdateHemoglobin,self).form_valid(form)

    success_url = reverse_lazy('account_hemoglobin')
    
class DeleteHemoglobin(DeleteView):

    template_name = 'delete_hemoglobin.html'
    model = Hemoglobin

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.delete()
       messages.success(request, u"¡Información eliminada con éxito!")
       return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('account_hemoglobin')


def list_hemoglobin_top(request, **kwargs):

    data = {}

    if kwargs:
        user_account = kwargs['pk']
        object_hemoglobin = Hemoglobin.objects.order_by('-id').filter(user_id = user_account)[:1]
    else:
        user_account = request.user
        object_hemoglobin = Hemoglobin.objects.order_by('-id').filter(user_id = user_account.id)[:1]
      
    if object_hemoglobin.count() == 1:
        
        data['percent'] = object_hemoglobin[0].percent
        data['timestamp_hemoglobin'] = object_hemoglobin[0].timestamp
    
    return data


def graphic_hemoglobin(request, **kwargs):

    data = {}

    if kwargs:
        user_account = kwargs['pk']
        object_hemoglobin = Hemoglobin.objects.order_by('-id').filter(user_id = user_account)
    else:
        user_account = request.user
        object_hemoglobin = Hemoglobin.objects.order_by('-id').filter(user_id = user_account.id)

    exchange = {}
    for ex in object_hemoglobin:
            exchange[ex.timestamp.strftime('%Y%m%dT%H%M%S')] = str(ex.percent)
               
    hemoglobin = [
                   {u'data': exchange,u'name': u'porcentaje'},  
                 ]

    data['line_1'] = hemoglobin
 
    return data
    
