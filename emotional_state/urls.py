from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	    url(r'^account/emotionalstates/$' ,ListEmotionalState.as_view(), name='account_emotionalstates'),
        url(r'^account/create/emotionalstates/$' ,AddEmotionalState.as_view(), name='account_create_emotionalstates'),
        url(r'^account/update/emotionalstates/(?P<pk>\d+)/$' ,UpdateEmotionalState.as_view(), name='account_update_emotionalstates'),
        url(r'^account/delete/emotionalstates/(?P<pk>\d+)/$' ,DeleteEmotionalState.as_view(), name='account_delete_emotionalstates'),
        
        
       
) 