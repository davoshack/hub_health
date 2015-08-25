# -*- coding: utf-8 -*-
import os, sys


from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy

from .models import *

from django.views.generic.edit import *
from django.views.generic import *

from django.contrib import messages


class AddGlycemia(CreateView):
    template_name = 'edit_glycemia.html'
    form_class = GlycemiaForm
    
    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
    	messages.success(self.request, u"¡Información guardada con éxito!")
    	return super(AddGlycemia,self).form_valid(form)
    
    success_url = reverse_lazy('account_glycemia')
    
     
class ListGlycemia(ListView):
    template_name = 'glycemia.html'
    form_class = GlycemiaForm

    success_url = reverse_lazy('account_glycemia')
    
    def get_queryset(self):
        return Glycemia.objects.order_by('-id').filter(user_id = self.request.user)
    
class UpdateGlycemia(UpdateView):
    template_name = 'edit_glycemia.html'
    form_class = GlycemiaForm
    model = Glycemia
    def form_valid(self,form):
    	self.object = form.save(commit=False)
    	self.object.user = self.request.user
    	self.object.save()
        messages.success(self.request, u"¡Información actualizada con éxito!")
    	return super(UpdateGlycemia,self).form_valid(form)
    success_url = reverse_lazy('account_glycemia')
    
class DeleteGlycemia(DeleteView):
    template_name = 'delete_glycemia.html'
    model = Glycemia
    
    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.delete()
       messages.success(request, u"¡Información eliminada con éxito!")
       return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('account_glycemia')
    
    
    
def list_glycemia_top(request, **kwargs):

    data = {}
    
    if kwargs:
        user_account = kwargs['pk']
        object_glycemia = Glycemia.objects.order_by('-id').filter(user_id = user_account)[:1]
    else:
        user_account = request.user
        object_glycemia = Glycemia.objects.order_by('-id').filter(user_id = user_account.id)[:1]
   

    if object_glycemia.count() == 1:
    
        data['measurement'] = object_glycemia[0].measurement
        data['context'] = object_glycemia[0].measurement_context
        data['blood_type'] = object_glycemia[0].blood_type
        data['timestamp_glycemia'] = object_glycemia[0].timestamp
    
    return data


def graphic_glycemia(request, **kwargs):

    data = {}

    if kwargs:
        user_account = kwargs['pk']
        object_glycemia = Glycemia.objects.order_by('-id').filter(user_id = user_account)
    else:
        user_account = request.user
        object_glycemia = Glycemia.objects.order_by('-id').filter(user_id = user_account.id)


    exchange = {}

    for ex in object_glycemia:
            exchange[ex.timestamp.strftime('%Y%m%dT%H%M%S')] = str(ex.measurement)
    
    glycemia = [
                   {u'data': exchange,u'name': u'glicemia'},
                   
               ]

    data['line_1'] = glycemia
 

    return data
   

    
