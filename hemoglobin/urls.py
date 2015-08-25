from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^account/hemoglobin/$' ,ListHemoglobin.as_view(), name='account_hemoglobin'),
        url(r'^account/create/hemoglobin/$' ,AddHemoglobin.as_view(), name='account_create_hemoglobin'),
        url(r'^account/update/hemoglobin/(?P<pk>\d+)/$' ,UpdateHemoglobin.as_view(), name='account_update_hemoglobin'),
        url(r'^account/delete/hemoglobin/(?P<pk>\d+)/$' ,DeleteHemoglobin.as_view(), name='account_delete_hemoglobin'),
             
) 