from django.conf.urls import patterns, url
from .views import AddContact

urlpatterns = patterns('',

        url(r'^directory/search/all/$', 'directory.views.search_directory_all', name='search_directory_all'),
        url(r'^directory/search/contacts/$', 'directory.views.search_directory_contacts', name='search_directory_contacts'),
        url(r'^directory/search/filter/specialtymedical/(?P<pk>\d+)/$', 'directory.views.filter_specialty_medical', name='search_filter_specialtymedical'),
        url(r'^directory/relationship/(?P<pk>\d+)/$', AddContact.as_view(), name='directory_relationship'),
        url(r'^directory/relationship/save/contact/(?P<id_contact>\d+)/$', 'directory.views.save_contact', name='directory_save_contact'),
        url(r'^directory/relationship/confirmed/contact/(?P<from_user>\d+)/(?P<state>\w+)/$', 'directory.views.confirmed_contact', name='confirmed_contact'),
        url(r'^directory/relationship/share/journal/(?P<from_user>\d+)/$', 'directory.views.share_journal_medic', name='share_journal'),
        url(r'^directory/relationship/not_share/journal/(?P<from_user>\d+)/$', 'directory.views.not_share_journal_medic', name='not_share_journal'),


)