from django.conf.urls import patterns, include, url


urlpatterns = patterns('',  # url(r'^account/init/$' ,Init.as_view(), name='account_init'),
                       url(r'^account/init/$', 'data_users.views.init', name='account_init'),
                       url(r'^account/profile/$', 'data_users.views.profile_user', name='account_profile'),
                       url(r'^account/edit/profile/$', 'data_users.views.edit_profile_user',
                           name='account_edit_profile'),
                       url(r'^account/medical_journal/$', 'data_users.views.medical_journal_user',
                           name='account_medical_journal'),
                       url(r'^account/edit/privacy_setting/$', 'data_users.views.edit_privacy_settings',
                           name='account_edit_privacy_settings'),

                       )