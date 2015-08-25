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

#----------Estado de Animo -------------------------------------------------------- 
class AddEmotionalState(CreateView):

    template_name = 'edit_emotional_state.html'
    form_class = EmotionalStatesForm
 
    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Información guardada con éxito!")
    	return super(AddEmotionalState,self).form_valid(form)
        
    success_url = reverse_lazy('account_emotionalstates')
    

        
class ListEmotionalState(ListView):

    template_name = 'emotional_state.html'
    form_class = EmotionalStatesForm

    success_url = reverse_lazy('account_emotionalstates')
    
       
    def get_queryset(self):
        return EmotionalStatesPatient.objects.order_by('-id').filter(user_id = self.request.user)

    
class UpdateEmotionalState(UpdateView):

    template_name = 'edit_emotional_state.html'
    form_class = EmotionalStatesForm
    model = EmotionalStatesPatient
   
    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Información actualizada con éxito!")
    	return super(UpdateEmotionalState,self).form_valid(form)

    success_url = reverse_lazy('account_emotionalstates')

    
class DeleteEmotionalState(DeleteView):

    template_name = 'delete_emotional_state.html'
    model = EmotionalStatesPatient

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.delete()
       messages.success(request, u"¡Información eliminada con éxito!")
       return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('account_emotionalstates')


def list_emotional_states_top(request, **kwargs):

    data = {}

    if kwargs:
        user_account = kwargs['pk']
        object_emotional_state = EmotionalStatesPatient.objects.order_by('-id').filter(user_id = user_account)[:1]
    else:
        user_account = request.user
        object_emotional_state = EmotionalStatesPatient.objects.order_by('-id').filter(user_id = user_account.id)[:1]
   
    
    if object_emotional_state.count() == 1:
        
        data['state'] = object_emotional_state[0].state
        data['timestamp_emotionalstates'] = object_emotional_state[0].timestamp
    
    return data


def graphic_emotionalstate(request, **kwargs):

    data = {}


    if kwargs:
        user_account = kwargs['pk']
        object_emotional_state = EmotionalStatesPatient.objects.order_by('-id').filter(user_id = user_account)
    else:
        user_account = request.user
        object_emotional_state = EmotionalStatesPatient.objects.order_by('-id').filter(user_id = user_account.id)

    exchange = {}
    for ex in object_emotional_state:
            exchange[ex.timestamp.strftime('%Y%m%dT%H%M%S')] = str(ex.state)
               
    emotional_state = [{u'data': exchange, u'name': u'puntuación'}]

    data['emotional_state_line'] = emotional_state
 
    return data
    