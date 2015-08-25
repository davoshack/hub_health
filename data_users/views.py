# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from .models import *
from specialist.models import *
from glucoday.models import *
from profile_lipids.models import *
from blood_pressure.models import *
from weight_size.models import *
from hemoglobin.models import *
from emotional_state.models import *
from symptoms.models import *
from gyneco.models import Gynecological
from django.views.generic.edit import *
from django.template import RequestContext
from datetime import datetime
from .forms import ProfileUserForm, MedicalConsultationForm
from registration.models import RegistrationProfile
from clubs.models import SubscriptionClubDoctor
from django.contrib import messages
from glucoday.views import list_glycemia_top
from profile_lipids.views import list_colesterol_top
from blood_pressure.views import list_blood_pressure_top
from weight_size.views import list_size_top, list_weight_top
from emotional_state.views import list_emotional_states_top
from hemoglobin.views import list_hemoglobin_top
from symptoms.views import list_generalsymptoms_top, list_glycemicsymptoms_top
from gyneco.views import list_gyneco_top


def init(request):
    args = {}

    user_login = request.user
    # user_object = ProfileUser.objects.filter(user_id=user_login.id)
    user_object_professional = ProfessionalProfile.objects.filter(user_id=user_login.id)
    user_object_academic = AcademicProfile.objects.filter(user_id=user_login.id)
    user_object_employment = EmploymentHistory.objects.filter(user_id=user_login.id)
    user_object_glycemic = Glycemia.objects.filter(user_id=user_login.id)
    user_object_blood_pressure = Pressure.objects.filter(user_id=user_login.id)
    user_object_profile_lipids = Colesterol.objects.filter(user_id=user_login.id)
    user_object_weight = Weight.objects.filter(user_id=user_login.id)
    user_object_size = Size.objects.filter(user_id=user_login.id)
    user_object_hemoglobin = Hemoglobin.objects.filter(user_id=user_login.id)
    user_object_emotional = EmotionalStatesPatient.objects.filter(user_id=user_login.id)
    user_object_general_symptoms = GeneralSymptoms.objects.filter(user_id=user_login.id)
    user_object_glycemics_symptoms = SymptomsGlycemicAlteration.objects.filter(user_id=user_login.id)
    user_object_gyneco = Gynecological.objects.filter(user_id=user_login.id)

    args['professional'] = user_object_professional
    args['academic'] = user_object_academic
    args['employment'] = user_object_employment
    args['glycemic'] = user_object_glycemic
    args['blood_pressure'] = user_object_blood_pressure
    args['colesterol'] = user_object_profile_lipids
    args['weight'] = user_object_weight
    args['size'] = user_object_size
    args['hemoglobin'] = user_object_hemoglobin
    args['emotional'] = user_object_emotional
    args['general_symptoms'] = user_object_general_symptoms
    args['glycemics_symptoms'] = user_object_glycemics_symptoms
    args['gyneco'] = user_object_gyneco

    return render_to_response('init.html', args, context_instance=RequestContext(request))


def profile_user(request):

    user_login = request.user
    user_object = ProfileUser.objects.filter(user_id=user_login.id)
    user_clubs = SubscriptionClubDoctor.objects.order_by('club').filter(user_id=user_login.id)
    gender = user_object[0].sex
    blood = user_object[0].blood_group
    age = datetime.today().year - user_object[0].date_birth.year
    patient_abstract = user_object[0].patient_abstract
    professional_abstract = user_object[0].professional_abstract
    medical_specialty = user_object[0].medical_specialty
    medical_emphasis = user_object[0].medical_emphasis
    nationality = user_object[0].nationality
    professional_register = user_object[0].professional_register
    blog = user_object[0].blog
    twitter = user_object[0].twitter
    facebook = user_object[0].facebook
    linkedin = user_object[0].linkedin
    youtube = user_object[0].you_tube

    object_profile = RegistrationProfile.objects.filter(user_id=user_login.id)
    type_user = object_profile[0].tipo_usuario

    medical_consultation = user_object[0].medical_consultation
    flag_blood = user_object[0].flag_blood
    flag_date_birth = user_object[0].flag_date_birth
    flag_patient_abstract = user_object[0].flag_patient_abstract
    flag_nationality = user_object[0].flag_nationality
    flag_message = user_object[0].flag_message

    args = {}
    args.update(csrf(request))

    args['type_user'] = type_user
    args['age'] = age
    args['gender'] = gender
    args['blood'] = blood
    args['patient_abstract'] = patient_abstract
    args['professional_abstract'] = professional_abstract
    args['nationality'] = nationality
    args['professional_register'] = professional_register
    args['medical_specialty'] = medical_specialty
    args['medical_emphasis'] = medical_emphasis
    args['medical_consultation'] = medical_consultation
    args['flag_blood'] = flag_blood
    args['flag_date_birth'] = flag_date_birth
    args['flag_patient_abstract'] = flag_patient_abstract
    args['flag_nationality'] = flag_nationality
    args['flag_message'] = flag_message
    args['blog'] = blog
    args['twitter'] = twitter
    args['facebook'] = facebook
    args['linkedin'] = linkedin
    args['youtube'] = youtube
    args['clubs'] = user_clubs

    return render_to_response('user_profile.html', args, context_instance=RequestContext(request))


def edit_profile_user(request):

    if request.method == 'POST':
        form = ProfileUserForm(request.POST, request.FILES, instance=request.user.profile_user)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Información actualizada con éxito!")
            return HttpResponseRedirect('/account/profile/')
    else:
        user = request.user
        profile_user = user.profile_user
        form = ProfileUserForm(instance=profile_user)

    user_login = request.user
    object_profile = RegistrationProfile.objects.filter(user_id=user_login.id)
    type_user = object_profile[0].tipo_usuario
    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['type_user'] = type_user

    return render_to_response('edit_profile.html', args, context_instance=RequestContext(request))


def edit_privacy_settings(request):

    if request.method == 'POST':
        form = MedicalConsultationForm(request.POST, request.FILES, instance=request.user.profile_user)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Información actualizada con éxito!")
            return HttpResponseRedirect('/account/profile/')
    else:
        user = request.user
        profile_user = user.profile_user
        form = MedicalConsultationForm(instance=profile_user)

    user_login = request.user
    object_profile = RegistrationProfile.objects.filter(user_id=user_login.id)
    type_user = object_profile[0].tipo_usuario
    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['type_user'] = type_user

    return render_to_response('edit_privacy_settings.html', args, context_instance=RequestContext(request))


def medical_journal_user(request):


    args = {}
    args.update(list_glycemia_top(request))
    args.update(list_colesterol_top(request))
    args.update(list_blood_pressure_top(request))
    args.update(list_weight_top(request))
    args.update(list_size_top(request))
    args.update(list_emotional_states_top(request))
    args.update(list_hemoglobin_top(request))
    args.update(list_generalsymptoms_top(request))
    args.update(list_glycemicsymptoms_top(request))
    args.update(list_gyneco_top(request))
    args.update(csrf(request))

    return render_to_response('medical_journal.html', args, context_instance=RequestContext(request))