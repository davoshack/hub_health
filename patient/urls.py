from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',

        url(r'^utilities/init/$', PatientUtilitiesInit.as_view(), name='utilities_init'),
        url(r'^patient/profile/public/(?P<pk>\d+)/$', ProfilePublic.as_view(), name='patient_profile_public'),
        url(r'^patient/profile/medical_journal/(?P<pk>\d+)/$', 'patient.views.profile_medical_journal', name='profile_medical_journal'),
        url(r'^patient/profile/graphic/glycemia/(?P<pk>\d+)/$', 'graphics.views.view_graphic_glycemia', name='profile_graphic_glycemia'),
        url(r'^patient/profile/graphic/profile_lipids/(?P<pk>\d+)/$', 'graphics.views.view_graphic_profile_lipids', name='profile_graphic_profile_lipids'),
        url(r'^patient/profile/graphic/blood_pressure/(?P<pk>\d+)/$', 'graphics.views.view_graphic_blood_pressure', name='profile_graphic_blood_pressure'),
        url(r'^patient/profile/graphic/weight/(?P<pk>\d+)/$', 'graphics.views.view_graphic_weight', name='profile_graphic_weight'),
        url(r'^patient/profile/graphic/size/(?P<pk>\d+)/$', 'graphics.views.view_graphic_size', name='profile_graphic_size'),
        url(r'^patient/profile/graphic/hemoglobin/(?P<pk>\d+)/$', 'graphics.views.view_graphic_hemoglobin', name='profile_graphic_hemoglobin'),
        url(r'^patient/profile/graphic/generalsymptoms/(?P<pk>\d+)/$', 'graphics.views.view_graphic_generalsymptoms', name='profile_graphic_generalsymptoms'),
        url(r'^patient/profile/graphic/glycemicsymptoms/(?P<pk>\d+)/$', 'graphics.views.view_graphic_glycemicsymptoms', name='profile_graphic_glycemicsymptoms'),
        url(r'^patient/profile/graphic/emotionalstate/(?P<pk>\d+)/$', 'graphics.views.view_graphic_emotionalstate', name='profile_graphic_emotionalstate'),
             
) 