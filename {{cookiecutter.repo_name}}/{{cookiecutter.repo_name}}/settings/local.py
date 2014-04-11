import sys
from .base import *
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}