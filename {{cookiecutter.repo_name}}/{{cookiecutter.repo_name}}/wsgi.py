"""
WSGI config for {{ cookiecutter.repo_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.repo_name }}.settings")

from dj_static import Cling, MediaCling
from django.core.wsgi import get_wsgi_application

application = Cling(MediaCling(get_wsgi_application()))