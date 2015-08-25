from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

	url(r'^utilities/foodroutines/$' ,ListFoodRoutines.as_view(), name='utilities_foodroutines'),
    url(r'^utilities/create/foodroutines/$' ,AddFoodRoutines.as_view(), name='utilities_create_foodroutines'),
    url(r'^utilities/update/foodroutines/(?P<pk>\d+)/$' ,UpdateFoodRoutines.as_view(), name='utilities_update_foodroutines'),
    url(r'^utilities/delete/foodroutines/(?P<pk>\d+)/$' ,DeleteFoodRoutines.as_view(), name='utilities_delete_foodroutines'),
             
) 