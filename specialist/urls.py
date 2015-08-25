from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',

        #url(r'^account/init/$' ,Init.as_view(), name='account_init'),
        url(r'^specialist/profile/(?P<pk>\d+)/$' ,SpecialistProfile.as_view(), name='specialist_profile'),
        url(r'^specialist/profile/public/(?P<pk>\d+)/$' ,SpecialistProfilePublic.as_view(), name='specialist_profile_public'),

        url(r'^specialist/professional/$' ,ListProfessionalProfile.as_view(), name='specialist_professional'),
        url(r'^specialist/create/professional/$' ,AddProfessionalProfile.as_view(), name='specialist_create_professional'),
        url(r'^specialist/update/professional/(?P<pk>\d+)/$' ,UpdateProfessionalProfile.as_view(), name='specialist_update_professional'),
        url(r'^specialist/delete/professional/(?P<pk>\d+)/$' ,DeleteProfessionalProfile.as_view(), name='specialist_delete_professional'),

        url(r'^specialist/academic/$' ,ListAcademicProfile.as_view(), name='specialist_academic'),
        url(r'^specialist/create/academic/$' ,AddAcademicProfile.as_view(), name='specialist_create_academic'),
        url(r'^specialist/update/academic/(?P<pk>\d+)/$' ,UpdateAcademicProfile.as_view(), name='specialist_update_academic'),
        url(r'^specialist/delete/academic/(?P<pk>\d+)/$' ,DeleteAcademicProfile.as_view(), name='specialist_delete_academic'),


        url(r'^specialist/employmenthistory/$' ,ListEmploymentHistory.as_view(), name='specialist_employmenthistory'),
        url(r'^specialist/create/employmenthistory/$' ,AddEmploymentHistory.as_view(), name='specialist_create_employmenthistory'),
        url(r'^specialist/update/employmenthistory/(?P<pk>\d+)/$' ,UpdateEmploymentHistory.as_view(), name='specialist_update_employmenthistory'),
        url(r'^specialist/delete/employmenthistory/(?P<pk>\d+)/$' ,DeleteEmploymentHistory.as_view(), name='specialist_delete_employmenthistory'),

        url(r'^specialist/create/entry/$' ,AddEntryBlog.as_view(), name='specialist_create_entry'),
        
)