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

class AddFoodRoutines(CreateView):
    template_name = 'edit_foodroutines.html'
    form_class = FoodRoutinesForm
 
    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Alimento guardado con éxito!")
    	return super(AddFoodRoutines,self).form_valid(form)
    success_url = reverse_lazy('utilities_foodroutines')

     
class ListFoodRoutines(ListView):
    template_name = 'foodroutines.html'
    form_class = FoodRoutinesForm

    success_url = reverse_lazy('utilities_foodroutines')
    
    def get_queryset(self):
        return FoodRoutines.objects.order_by('-id').filter(user_id = self.request.user)
    
class UpdateFoodRoutines(UpdateView):
    template_name = 'edit_foodroutines.html'
    form_class = FoodRoutinesForm
    model = FoodRoutines

    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Alimento actualizado con éxito!")
    	return super(UpdateFoodRoutines,self).form_valid(form)
    success_url = reverse_lazy('utilities_foodroutines')
    
class DeleteFoodRoutines(DeleteView):
    template_name = 'delete_foodroutines.html'
    model = FoodRoutines

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.delete()
       messages.success(request, u"¡Alimento eliminado con éxito!")
       return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('utilities_foodroutines')