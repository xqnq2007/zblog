"""
WSGI config for zblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys 
sys.path.append('/usr/local/lib/python3.5/dist-packages')
from django.core.wsgi import get_wsgi_application

path = '/home/pyprojects/zblog'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zblog.settings")

application = get_wsgi_application()
