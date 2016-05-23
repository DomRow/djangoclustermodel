
"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

from djangoApp import clusters
import os,sys

project_path = "/Users/user/Envs/djangonew4/"

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
sys.path.append(project_path)
os.chdir(project_path)

application = get_wsgi_application()

def alternate():
	data='FROM WSGI: '
	return (data)


