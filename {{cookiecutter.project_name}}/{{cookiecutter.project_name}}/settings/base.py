"""
Base django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", False)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv("DJANGO_DEBUG", "0")) # TODO: make this work when DJANGO_DEBUG is set to Fale or True as well
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")


########## APPLICATON DEFINITION
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = (
    'south',
)

LOCAL_APPS = (
    '{{ cookiecutter.project_name }}',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APPLICATON DEFINITION


ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{cookiecutter.project_name}}.wsgi.application'

# A tuple that lists people who get code error notifications when DEBUG=False
ADMINS = (
    ("{{ cookiecutter.author_name }}", "{{ cookiecutter.email }}")
)

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config()}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "fixtures"),
)


########## INTERNATIONALIZATION
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = '{{ cookiecutter.language_code }}'

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = True

USE_TZ = True
########## END INTERNATIONALIZATION

STATIC_URL = os.getenv("DJANGO_STATIC_URL", '/static/')
MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", '/media/')
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", 'public/static')
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", 'public/media')
