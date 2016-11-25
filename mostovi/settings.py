"""
Django settings for mostovi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5h%-(0%8#m_8ftt_#kh831)g8uw*jy9mtaz^zalr6$$^==lb&c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['pokreativnipoti.fgg.uni-lj.si']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'baza',
    'home',
    'login',
    'about',
		'haystack',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mostovi.urls'

WSGI_APPLICATION = 'mostovi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mostovi',
	'USER': 'postgres',
	'PASSWORD': 'PkPdPzo1-SerV',
	'HOST': 'localhost',
	'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'sl_SI'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = 'http://pokreativnipoti.fgg.uni-lj.si/static/'
STATIC_ROOT = '/var/www/static/'
MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = 'http://pokreativnipoti.fgg.uni-lj.si/media/'
#TEMPLATE_ROOT = ('http://88.200.33.216/templates/')
#TEMPLATE_LOADERS = 'django.template.loaders.filesystem.Loader'
TEMPLATE_DIRS = (
    os.path.dirname(__file__) + '/templates',
)

DATETIME_INPUT_FORMATS=(
	'%d. %m. %Y %H:%M:%S',
)
FILE_UPLOAD_MAX_MEMORY_SIZE = 102428800
FIRST_DAY_OF_WEEK = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'weiss.simon.1995@gmail.com'
EMAIL_HOST_PASSWORD = 'grece759'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'weiss.simon.1995@gmail.com'
