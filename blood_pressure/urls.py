from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^account/blood_pressure/$' ,ListPressure.as_view(), name='account_blood_pressure'),
    url(r'^account/create/blood_pressure/$' ,AddPressure.as_view(), name='account_create_blood_pressure'),
    url(r'^account/update/blood_pressure/(?P<pk>\d+)/$' ,UpdatePressure.as_view(), name='account_update_blood_pressure'),
    url(r'^account/delete/blood_pressure/(?P<pk>\d+)/$' ,DeletePressure.as_view(), name='account_delete_blood_pressure'),
       
)