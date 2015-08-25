from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	    url(r'^utilities/drugs/$' ,ListDrugs.as_view(), name='utilities_drugs'),
        url(r'^utilities/create/drugs/$' ,AddDrugs.as_view(), name='utilities_create_drugs'),
        url(r'^utilities/update/drugs/(?P<pk>\d+)/$' ,UpdateDrugs.as_view(), name='utilities_update_drugs'),
        url(r'^utilities/delete/drugs/(?P<pk>\d+)/$' ,DeleteDrugs.as_view(), name='utilities_delete_drugs'),
        
        
       
) 