from django.core import serializers
from models import *
from forms import ClusterForm
from tests.testblobs import blob1,rings1,crescent1
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.template.response import TemplateResponse,Template,Context
from django.shortcuts import render_to_response
import random, json


def index(request):
	template = loader.get_template('index.html')
	return render(request,'index.html')


def pured3(request):
	dataset=(request.POST.get('dataset'))
	algorithm=(request.POST.get('algorithm'))
	numres=(request.POST.get('numresults'))
	klust=int(request.POST.get('clusters'))


	if dataset=='IMDB - Ratings':
	 	settype="ratings"
	 	initrows=Movies_all.values_list('rating_count','rating','title').exclude(rating_count__gte=100).exclude(rating_count__lt=1)[:numres]
	 	rows=[]
	 	for i,e in enumerate(initrows):
	 		x=(e[1]*10)
	 		rows.append((e[0],int(x),e[2]))
	if dataset=='IMDB - Actors':
		settype="actors"
		#rows=Actors_all.values_list('fullname','movie_ref')
		rows=Actors.objects.filter(movie_ref__title__contains="Black")
		print rows[1].movie_ref
	elif dataset=='Iris':
	 	settype="iris"
	 	rows=Iris_all.values_list('sepal_width','petal_length','species')[:numres]
	elif dataset=='Blobs':
	 	print blob1
	 	settype="blobs"
		rows=blob1
	elif dataset=='Rings':
		settype="rings"
		rows=rings1	
	elif dataset=='Crescents':
		settype="crescents"
	 	rows=crescent1
	else: return 0
	
	clusted=k_means(rows,k=klust)

	##Context takes two variables - a dictionary mapping var names to var vals
	##These vars are made available on scatter page
	context = RequestContext(request, {
		'data': json.dumps(clusted),
		'settype': json.dumps(settype), 
		'dataset':dataset,
		'clusters':klust
		})
	
	return render(request, 'scatterchart.html',context) 