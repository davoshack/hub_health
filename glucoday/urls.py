from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^account/glycemia/$' ,ListGlycemia.as_view(), name='account_glycemia'),
    url(r'^account/create/glycemia/$' ,AddGlycemia.as_view(), name='account_create_glycemia'),
    url(r'^account/update/glycemia/(?P<pk>\d+)/$' ,UpdateGlycemia.as_view(), name='account_update_glycemia'),
    url(r'^account/delete/glycemia/(?P<pk>\d+)/$' ,DeleteGlycemia.as_view(), name='account_delete_glycemia'),
               
) 