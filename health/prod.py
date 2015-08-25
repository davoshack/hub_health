"""
Django settings for hubsalud project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_ID = 1



# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'werkzeug',
    'tagging',
    'mptt',
    'mockups',
    'django_extensions',
    'zinnia',
    'zinnia_ckeditor',
    'ckeditor',
    'registration',
    'widget_tweaks',
    'sorl.thumbnail',
    'data_users',
    'emotional_state',
    'glucoday',
    'graphics',
    'blood_pressure',
    'clubs',
    'dating',
    'drugs',
    'hemoglobin',
    'laboratory',
    'gyneco',
    'patient',
    'profile_lipids',
    'qandr',
    'routines',
    'specialist',
    'symptoms',
    'weight_size',
    'audios',
    'directory',
    'postman',
    'relationships',
    'chartkick',
    'pybb',
)

import chartkick

STATICFILES_DIRS = (
    chartkick.js(),
)

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
    'zinnia-content': {
        'toolbar_Zinnia': [
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Undo', 'Redo'],
            ['Scayt'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Source'],
            ['Maximize'],
            '/',
            ['Bold', 'Italic', 'Underline', 'Strike',
             'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-',
             'Outdent', 'Indent', '-', 'Blockquote'],
            ['Styles', 'Format'],
        ],
        'toolbar': 'Zinnia',
    },
}



ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

"""Settings django-postman"""
POSTMAN_DISALLOW_MULTIRECIPIENTS = True
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_SHOW_USER_AS = 'get_full_name'

AJAX_LOOKUP_CHANNELS = {'users': {'model': 'auth.user', 'search_field': 'username'}, }
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_AUTOCOMPLETER_APP = {'arg_default': 'users', }

PYBB_TOPIC_PAGE_SIZE = 10
PYBB_FORUM_PAGE_SIZE = 10


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pybb.middleware.PybbMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'postman.context_processors.inbox',
    'health.context_processors.load_profile',
    'pybb.context_processors.processor',
)

"""
TEMPLATE_DIRS = (
   RUTA_PROYECTO.child('templates')

)
"""

"""Settings redirections login"""
LOGIN_REDIRECT = '/account/init/'
LOGIN_REDIRECT_PROFILE_SETTING = '/account/profileactive/'

ROOT_URLCONF = 'health.urls'

WSGI_APPLICATION = 'health.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True



ZINNIA_PAGINATION = 5
MEDIA_URL = '/registration/static/registration/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['/registration/static/registration/'])
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)












