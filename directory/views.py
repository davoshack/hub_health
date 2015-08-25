# -*- coding: utf-8 -*-

from data_users.models import MedicalEspecialty, ProfileUser
from directory.forms import SearchDirectoryForm
from directory.models import Contacts
from django.contrib import messages
from django.shortcuts import render_to_response, resolve_url
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from relationships.models import *

"""
class Directory(TemplateView):
    template_name = "directory.html"

    def get_context_data(self, **kwargs):
        args = super(Directory, self).get_context_data(**kwargs)

        object_user = User.objects.order_by('last_name').all()
        args['clubs_members'] = object_user

        return args
"""


def search_directory_all(request):

    args = {}
    user_login = request.user

    if request.method == "POST":
        form = SearchDirectoryForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            object_user = User.objects.order_by('last_name').filter(first_name__icontains=first_name).filter(last_name__icontains=last_name)
            args['clubs_members'] = object_user
            args['form'] = form
            args['first_name'] = first_name
            args['last_name'] = last_name

    else:

        form = SearchDirectoryForm(request.POST)
        object_specialty = MedicalEspecialty.objects.all()
        object_user = User.objects.all().order_by('last_name')
        object_contacts = Contacts.objects.filter(from_user=user_login)

        user_all = []
        for u in object_user:
            user_all.append(u)

        for l in object_user:
            for j in object_contacts:

                if l.id == j.to_user:
                    user_all.remove(l)



        args['user_all'] = user_all
        args['form'] = form
        args['specialty_medical'] = object_specialty

    return render_to_response('directory.html', args, context_instance=RequestContext(request))


def filter_specialty_medical(request, **kwargs):

    args = {}

    if request.method == "POST":
        form = SearchDirectoryForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

    else:
        form = SearchDirectoryForm(request.POST)

    id_specialty_medical = kwargs['pk']
    object_specialty = MedicalEspecialty.objects.all()
    object_user = ProfileUser.objects.filter(medical_specialty=id_specialty_medical)
    args['form'] = form
    args['directory'] = object_user
    args['specialty_medical'] = object_specialty

    return render_to_response('filter_specialty_medical.html', args, context_instance=RequestContext(request))


def search_directory_contacts(request):

    args = {}
    user_login = request.user
    object_contacts = Contacts.objects.filter(from_user=user_login)
    object_user = User.objects.all()
    confirmed = []
    unconfirmed = []
    rejected = []

    if object_contacts.count() != 0:

        for i in object_contacts:
            for j in object_user:
                if i.to_user == j.id and i.state == 'confirmed':
                    confirmed.append(j)
                if i.to_user == j.id and i.state == 'unconfirmed':
                    unconfirmed.append(j)
                if i.to_user == j.id and i.state == 'rejected':
                    rejected.append(j)

        args['unconfirmed'] = unconfirmed
        args['confirmed'] = confirmed
        args['rejected'] = rejected

    else:
        args['contacts'] = "not"

    args['list_to_user_contact'] = list_to_user_contact(request)

    return render_to_response('contacts.html', args, context_instance=RequestContext(request))


def list_to_user_contact(request):

    user_login = request.user
    object_contacts = Contacts.objects.filter(to_user=user_login.id).filter(state='unconfirmed')

    return object_contacts


class AddContact(TemplateView):
    template_name = "add_contact_confirm.html"

    def get_context_data(self, **kwargs):
        args = super(AddContact, self).get_context_data(**kwargs)
        user_id = kwargs['pk']
        name = User.objects.filter(id=user_id)
        args['first_name_user'] = name[0].first_name
        args['last_name_user'] = name[0].last_name
        args['id'] = name[0].id

        return args


def confirmed_contact(request, **kwargs):

    state = kwargs['state']
    from_user = kwargs['from_user']
    user_login = request.user
    object_contacts = Contacts.objects.get(to_user=user_login.id, state='unconfirmed', from_user=from_user)

    if state == "Confirmed":
        object_contacts.state = 'confirmed'
        object_new = Contacts(from_user=user_login, to_user=from_user, state="confirmed")
        object_new.save()
        messages.success(request, u"¡Solicitud de contacto confirmada con éxito!")
    elif state == 'Rejected':
        object_contacts.state = 'rejected'
        messages.success(request, u"¡Solicitud de contacto rechazada con éxito!")

    object_contacts.save()

    return HttpResponseRedirect(resolve_url('search_directory_contacts'))


def save_contact(request, **kwargs):

    user_login = request.user
    id_contact = kwargs['id_contact']

    object_new = Contacts(from_user=user_login, to_user=id_contact, state="unconfirmed")
    object_new.save()
    messages.success(request, u"¡Solicitud de contacto enviada con éxito.!")

    return HttpResponseRedirect(resolve_url('search_directory_contacts'))


def share_journal_medic(request, **kwargs):

    from_user = kwargs['from_user']
    user_login = request.user
    object_from_user = Contacts.objects.get(to_user=user_login.id, from_user=from_user)
    object_from_user.state_share_journal = 1
    object_from_user.save()

    object_to_user = Contacts.objects.get(to_user=from_user, from_user=user_login.id)
    object_to_user.state_share_journal = 1
    object_to_user.save()

    messages.success(request, u"¡Permiso para acceso al diario médico realizado con éxito!")

    return HttpResponseRedirect(resolve_url('search_directory_contacts'))


def not_share_journal_medic(request, **kwargs):

    from_user = kwargs['from_user']
    user_login = request.user
    object_from_user = Contacts.objects.get(to_user=user_login.id, from_user=from_user)
    object_from_user.state_share_journal = 0
    object_from_user.save()

    object_to_user = Contacts.objects.get(to_user=from_user, from_user=user_login.id)
    object_to_user.state_share_journal = 0
    object_to_user.save()

    messages.success(request, u"¡Denegación de acceso al diario médico realizado con éxito!")

    return HttpResponseRedirect(resolve_url('search_directory_contacts'))