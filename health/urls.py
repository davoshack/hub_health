from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'health.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('data_users.urls')),
    url(r'^', include('emotional_state.urls')),
    url(r'^', include('glucoday.urls')),
    url(r'^', include('profile_lipids.urls')),
    url(r'^', include('clubs.urls')),
    url(r'^', include('specialist.urls')),
    url(r'^', include('patient.urls')),
    url(r'^', include('blood_pressure.urls')),
    url(r'^', include('weight_size.urls')),
    url(r'^', include('emotional_state.urls')),
    url(r'^', include('hemoglobin.urls')),
    url(r'^', include('graphics.urls')),
    url(r'^', include('symptoms.urls')),
    url(r'^', include('drugs.urls')),
    url(r'^', include('laboratory.urls')),
    url(r'^', include('routines.urls')),
    url(r'^', include('dating.urls')),
    url(r'^', include('gyneco.urls')),
    url(r'^', include('audios.urls')),
    url(r'^', include('directory.urls')),
    url(r'^', include('relationships.urls')),
    url(r'^messages/', include('postman.urls')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    
)

