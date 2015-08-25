# -*- coding: utf-8 -*-

from .forms import *
from django.core.urlresolvers import reverse_lazy

from .models import *

from django.views.generic.edit import *
from django.views.generic import *

from django.contrib import messages

# ----------Mediciones - Presion -----------------------------------------------------------------#
class AddPressure(CreateView):
    template_name = 'edit_blood_pressure.html'
    form_class = PressureForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información guardada con éxito!")
        return super(AddPressure, self).form_valid(form)

    success_url = reverse_lazy('account_blood_pressure')


class ListPressure(ListView):
    template_name = 'blood_pressure.html'
    form_class = PressureForm

    success_url = reverse_lazy('account_blood_pressure')

    def get_queryset(self):
        return Pressure.objects.order_by('-id').filter(user_id=self.request.user)


class UpdatePressure(UpdateView):
    template_name = 'edit_blood_pressure.html'
    form_class = PressureForm
    model = Pressure

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información actualizada con éxito!")
        return super(UpdatePressure, self).form_valid(form)

    success_url = reverse_lazy('account_blood_pressure')


class DeletePressure(DeleteView):
    template_name = 'delete_blood_pressure.html'
    model = Pressure

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, u"¡Información eliminada con éxito!")
        return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('account_blood_pressure')


def list_blood_pressure_top(request, **kwargs):
    data = {}

    if kwargs:
        user_account = kwargs['pk']
        object_blood_pressure = Pressure.objects.order_by('-id').filter(user_id=user_account)[:1]
    else:
        user_account = request.user
        object_blood_pressure = Pressure.objects.order_by('-id').filter(user_id=user_account.id)[:1]

    if object_blood_pressure.count() == 1:
        data['systolic'] = object_blood_pressure[0].systolic
        data['diastolic'] = object_blood_pressure[0].diastolic
        data['bpm'] = object_blood_pressure[0].bpm
        data['beat_status'] = object_blood_pressure[0].beat_status
        data['timestamp_pressure'] = object_blood_pressure[0].timestamp

    return data


def graphic_blood_pressure(request, **kwargs):
    data = {}

    if kwargs:
        user_account = kwargs['pk']
        object_blood_pressure = Pressure.objects.order_by('-id').filter(user_id=user_account)
    else:
        user_account = request.user
        object_blood_pressure = Pressure.objects.order_by('-id').filter(user_id=user_account.id)

    systolic_line = {}
    diastolic_line = {}
    bpm_line = {}

    for ex in object_blood_pressure:
        systolic_line[ex.timestamp.strftime('%Y%m%dT%H%M%S')] = str(ex.systolic)
    for ex in object_blood_pressure:
        diastolic_line[ex.timestamp.strftime('%Y%m%dT%H%M%S')] = str(ex.diastolic)

    for ex in object_blood_pressure:
        bpm_line[ex.timestamp.strftime('%Y%m%dT%H%M%S')] = str(ex.bpm)

    pressure_line = [{u'data': systolic_line, u'name': u'sistólica'},
                     {u'data': diastolic_line, u'name': u'diastólica'}]

    data['pressure'] = pressure_line

    data['bpm'] = bpm_line

    return data
