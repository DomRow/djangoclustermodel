#This file exposes a callable "application" variable 
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clustermodel.settings")

application = get_wsgi_application()
