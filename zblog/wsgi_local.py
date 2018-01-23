"""
WSGI config for zblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys 

from django.core.wsgi import get_wsgi_application
#sys.path.append('/Users/wang/pyprojects/virtualenv/zblogenv/lib/python3.6/site-packages')

path = '/Users/wang/pyprojects/zblog'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zblog.settings")

application = get_wsgi_application()
  