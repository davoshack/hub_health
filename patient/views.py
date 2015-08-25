# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from data_users.models import ProfileUser
from clubs.models import SubscriptionClubDoctor
from django.views.generic import *
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User
from glucoday.views import list_glycemia_top
from profile_lipids.views import list_colesterol_top
from blood_pressure.views import list_blood_pressure_top
from weight_size.views import list_size_top, list_weight_top
from emotional_state.views import list_emotional_states_top
from hemoglobin.views import list_hemoglobin_top
from symptoms.views import list_generalsymptoms_top, list_glycemicsymptoms_top


class ProfilePublic(TemplateView):
    template_name = "patient_profile_public.html"

    def get_context_data(self, **kwargs):
        args = super(ProfilePublic, self).get_context_data(**kwargs)
        id_user = kwargs['pk']
        names = User.objects.filter(id=id_user)
        user_object = ProfileUser.objects.filter(user_id=id_user)
        user_clubs = SubscriptionClubDoctor.objects.order_by('club').filter(user_id=id_user)
        avatar = user_object[0].image
        gender = user_object[0].sex
        blood = user_object[0].blood_group
        age = datetime.today().year - user_object[0].date_birth.year
        patient_abstract = user_object[0].patient_abstract
        nationality = user_object[0].nationality

        flag_blood = user_object[0].flag_blood
        flag_date_birth = user_object[0].flag_date_birth
        flag_patient_abstract = user_object[0].flag_patient_abstract
        flag_nationality = user_object[0].flag_nationality
        flag_message = user_object[0].flag_message

        blog = user_object[0].blog
        twitter = user_object[0].twitter
        facebook = user_object[0].facebook
        linkedin = user_object[0].linkedin
        youtube = user_object[0].you_tube

        args['flag_blood'] = flag_blood
        args['flag_date_birth'] = flag_date_birth
        args['flag_patient_abstract'] = flag_patient_abstract
        args['flag_nationality'] = flag_nationality
        args['flag_message'] = flag_message
        args['names'] = names
        args['avatar'] = avatar

        args['age'] = age
        args['gender'] = gender
        args['blood'] = blood
        args['patient_abstract'] = patient_abstract
        args['nationality'] = nationality
        args['blog'] = blog
        args['twitter'] = twitter
        args['facebook'] = facebook
        args['linkedin'] = linkedin
        args['youtube'] = youtube
        args['clubs'] = user_clubs
        args['id_user'] = id_user

        return args


def profile_medical_journal(request, **kwargs):

    id_user = kwargs['pk']
    names = User.objects.filter(id=id_user)

    args = {}
    args.update(list_glycemia_top(request, **kwargs))
    args.update(list_colesterol_top(request, **kwargs))
    args.update(list_blood_pressure_top(request, **kwargs))
    args.update(list_weight_top(request, **kwargs))
    args.update(list_size_top(request, **kwargs))
    args.update(list_emotional_states_top(request, **kwargs))
    args.update(list_hemoglobin_top(request, **kwargs))
    args.update(list_generalsymptoms_top(request, **kwargs))
    args.update(list_glycemicsymptoms_top(request, **kwargs))
    args['names'] = names

    return render_to_response('patient_profile_medical_journal.html', args, context_instance=RequestContext(request))


class PatientUtilitiesInit(TemplateView):
    template_name = "patient_utilities_init.html"

