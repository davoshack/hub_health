"""
URL patterns for the views included in ``django.contrib.auth``.

Including these URLs (via the ``include()`` directive) will set up the
following patterns based at whatever URL prefix they are included
under:

* User login at ``login/``.

* User logout at ``logout/``.

* The two-step password change at ``password/change/`` and
  ``password/change/done/``.

* The four-step password reset at ``password/reset/``,
  ``password/reset/confirm/``, ``password/reset/complete/`` and
  ``password/reset/done/``.

The default registration backend already has an ``include()`` for
these URLs, so under the default setup it is not necessary to manually
include these views. Other backends may or may not include them;
consult a specific backend's documentation for details.

"""


from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy

from .vistas_auth import logout, login, password_change, password_change_done, password_reset, password_reset_confirm, password_reset_complete, password_reset_done


urlpatterns = patterns('',
                       url(r'^login/$',
                           login,
                           {'template_name': 'login.html'},
                           name='auth_login'),
                       url(r'^logout/$',
                           logout,
                           {'template_name': 'logout.html'},
                           name='auth_logout'),
                       url(r'^password/change/$',
                           password_change,
                           {'post_change_redirect': reverse_lazy('password_change_done')},
                           name='password_change'),
                       url(r'^password/change/done/$',
                           password_change_done,
                           name='password_change_done'),
                       url(r'^password/reset/$',
                           password_reset,
                           name='auth_password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                           password_reset_confirm,
                           {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')},
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^password/reset/done/$',
                           password_reset_done,
                           name='auth_password_reset_done'),
)
