from models import Director,Actors,Movies,Genres
from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain
from django.template import Context, Template

Moviesall=Movies.objects.all()
#.objects.exclude(imid__gt=100)
x=Moviesall.values_list('rating_count',flat=True)[:1]
z=Moviesall.values_list('rating',flat=True)[:1]

list_1=Moviesall.values_list('rating',flat=True)[:1]
#list_2=Moviesall.values_list('rating_count',flat=True)[:1]
#list_all=list(chain(list_1, list_2))

# def cluster(num):
# 	list={}
# 	context={'list':list}
# 	return HttpResponse(context)


def cluster2(request,list_1):
	context={'listf':list_1}
	return HttpResponse(context.values())