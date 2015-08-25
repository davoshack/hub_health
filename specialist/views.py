# -*- encoding: utf-8 -*-
import os, sys


from django.core.urlresolvers import reverse, reverse_lazy
from data_users.models import ProfileUser
from clubs.models import SubscriptionClubDoctor
from audios.models import MedicalAudios
from django.views.generic.edit import *
from django.views.generic import *
from datetime import datetime
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages


# ---------------------------AcademicProfile-----------------------------------------------#
from zinnia.models import Author


class AddAcademicProfile(CreateView):
    template_name = 'edit_academicprofile.html'
    form_class = AcademicProfileForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información académica guardada con éxito!")
        return super(AddAcademicProfile, self).form_valid(form)

    success_url = reverse_lazy('specialist_academic')


class ListAcademicProfile(ListView):
    template_name = 'list_academicprofile.html'
    form_class = AcademicProfileForm

    success_url = reverse_lazy('specialist_academic')

    def get_queryset(self):
        return AcademicProfile.objects.order_by('-id').filter(user_id=self.request.user)


class UpdateAcademicProfile(UpdateView):
    template_name = 'edit_academicprofile.html'
    form_class = AcademicProfileForm
    model = AcademicProfile

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información académica actualizada con éxito!")
        return super(UpdateAcademicProfile, self).form_valid(form)

    success_url = reverse_lazy('specialist_academic')


class DeleteAcademicProfile(DeleteView):
    template_name = 'delete_academicprofile.html'
    model = AcademicProfile

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, u"¡Información académica eliminada con éxito!")
        return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('specialist_academic')


#---------------------------ProfessionalProfile-----------------------------------------------#  
class AddProfessionalProfile(CreateView):
    template_name = 'edit_professionalprofile.html'
    form_class = ProfessionalProfileForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información profesional guardada con éxito!")
        return super(AddProfessionalProfile, self).form_valid(form)

    success_url = reverse_lazy('specialist_professional')


class ListProfessionalProfile(ListView):
    template_name = 'list_professionalprofile.html'
    form_class = ProfessionalProfileForm

    success_url = reverse_lazy('specialist_professional')

    def get_queryset(self):
        return ProfessionalProfile.objects.order_by('-id').filter(user_id=self.request.user)


class UpdateProfessionalProfile(UpdateView):
    template_name = 'edit_professionalprofile.html'
    form_class = ProfessionalProfileForm
    model = ProfessionalProfile

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información profesional actualizada con éxito!")
        return super(UpdateProfessionalProfile, self).form_valid(form)

    success_url = reverse_lazy('specialist_professional')


class DeleteProfessionalProfile(DeleteView):
    template_name = 'delete_professionalprofile.html'
    model = ProfessionalProfile

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, u"¡Información profesional eliminada con éxito!")
        return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('specialist_professional')


#---------------------------EmploymentHistory-----------------------------------------------#
class AddEmploymentHistory(CreateView):
    template_name = 'edit_employmenthistoryprofile.html'
    form_class = EmploymentHistoryForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información laboral guardada con éxito!")
        return super(AddEmploymentHistory, self).form_valid(form)

    success_url = reverse_lazy('specialist_employmenthistory')


class ListEmploymentHistory(ListView):
    template_name = 'list_employmenthistoryprofile.html'
    form_class = EmploymentHistoryForm

    success_url = reverse_lazy('specialist_employmenthistory')

    def get_queryset(self):
        return EmploymentHistory.objects.order_by('-id').filter(user_id=self.request.user)


class UpdateEmploymentHistory(UpdateView):
    template_name = 'edit_employmenthistoryprofile.html'
    form_class = EmploymentHistoryForm
    model = EmploymentHistory

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, u"¡Información laboral actualizada con éxito!")
        return super(UpdateEmploymentHistory, self).form_valid(form)

    success_url = reverse_lazy('specialist_employmenthistory')


class DeleteEmploymentHistory(DeleteView):
    template_name = 'delete_employmenthistoryprofile.html'
    model = EmploymentHistory

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, u"¡Información laboral eliminada con éxito!")
        return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy('specialist_employmenthistory')


#---------------------------Blog--------------------------------------------·#
class AddEntryBlog(CreateView):
    template_name = 'edit_blog.html'
    form_class = EntryForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        form.cleaned_data['authors'] = Author.objects.filter(
                pk=self.request.user.pk)
        form.cleaned_data['slug'] = form.cleaned_data['title']

        self.object.save()
        messages.success(self.request,
                         u"¡Entrada creada con éxito, una vez sea aprobada se publicará en el blog de Hub Salud!")
        return super(AddEntryBlog, self).form_valid(form)

    success_url = reverse_lazy('specialist_create_entry')


class SpecialistProfilePublic(TemplateView):
    template_name = "profile_public.html"

    def get_context_data(self, **kwargs):
        context = super(SpecialistProfilePublic, self).get_context_data(**kwargs)
        id_user = kwargs['pk']
        names = User.objects.filter(id=id_user)
        objeto_user = ProfileUser.objects.filter(user_id=id_user)
        age = datetime.today().year - objeto_user[0].date_birth.year
        club = SubscriptionClubDoctor.objects.filter(user_id=id_user)
        professional_profile = ProfessionalProfile.objects.filter(user_id=id_user)
        audio = MedicalAudios.objects.filter(user_id=id_user)
        academic_profile = AcademicProfile.objects.filter(user_id=id_user)
        employment_history = EmploymentHistory.objects.filter(user_id=id_user)
        context['names'] = names
        context['club'] = club
        context['usr'] = objeto_user
        context['professional_profile'] = professional_profile
        context['audio'] = audio
        context['academic_profile'] = academic_profile
        context['employment_history'] = employment_history
        return context


class SpecialistProfile(TemplateView):
    template_name = "specialist_profile.html"

    def get_context_data(self, **kwargs):
        args = super(SpecialistProfile, self).get_context_data(**kwargs)
        id_user = kwargs['pk']
        names = User.objects.filter(id=id_user)
        user_object = ProfileUser.objects.filter(user_id=id_user)
        user_clubs = SubscriptionClubDoctor.objects.order_by('club').filter(user_id=id_user)
        avatar = user_object[0].image
        gender = user_object[0].sex

        blog = user_object[0].blog
        twitter = user_object[0].twitter
        facebook = user_object[0].facebook
        linkedin = user_object[0].linkedin
        youtube = user_object[0].you_tube

        args['gender'] = gender
        args['names'] = names
        args['avatar'] = avatar
        args['blog'] = blog
        args['twitter'] = twitter
        args['facebook'] = facebook
        args['linkedin'] = linkedin
        args['youtube'] = youtube
        args['clubs'] = user_clubs

        return args

