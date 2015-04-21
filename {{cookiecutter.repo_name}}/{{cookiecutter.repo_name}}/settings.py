"""
Base django settings for {{cookiecutter.repo_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", False)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", False) in ["True", "1", "yes", "true", "TRUE", "on", "ON", "On"]
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")



ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

# A tuple that lists people who get code error notifications when DEBUG=False
ADMINS = (
    ("{{ cookiecutter.author_name }}", "{{ cookiecutter.email }}")
)

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config()}

# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = '{{ cookiecutter.language_code }}'

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = os.getenv("DJANGO_STATIC_URL", '/static/')
MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", '/media/')
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", 'static')
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", 'media')

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = (
    'debug_toolbar',
    'django_extensions',
    'djangobower',
    # 'crispy_forms',
)

LOCAL_APPS = (
    '{{ cookiecutter.repo_name }}',
)

INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

BOWER_INSTALLED_APPS = (
    'bootstrap-sass#3.3.4',
    'jquery#<2'
    # 'underscore',
)

# E-mail:
SERVER_EMAIL = 'webserver <webserver@myhost.com>'
EMAIL_HOST = os.getenv("DJANGO_EMAIL_HOST", "localhost")
EMAIL_PORT = os.getenv("DJANGO_EMAIL_PORT", 587)
EMAIL_HOST_USER = os.getenv("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("DJANGO_EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = "Website <info@website.com>"

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
