from django.shortcuts import render
from django.http import HttpResponse
import datetime
from models import Film

films=Film.objects.all()

def index(request):
	film=films[1].title
	now = datetime.datetime.now()
	html = "<html><body>It is now %s</body></html>" % film
	return HttpResponse(html)

#results 