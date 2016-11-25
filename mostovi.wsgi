import os
import sys

sys.path.append('/web/mostovi/mostovi/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
