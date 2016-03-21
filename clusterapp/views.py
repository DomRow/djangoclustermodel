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
from django.db.models import Count
import random, json
import time

def index(request):

	template = loader.get_template('index.html')
	if request.method == 'POST':
		form = ClusterForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('cluster-results/')
	else:
		form =ClusterForm()	
	return render(request,'index.html', {'form': form})


def pured3(request):
	dataset=(request.POST.get('dataset'))
	algorithm=(request.POST.get('algorithm'))
	numres=(request.POST.get('numresults'))
	klust=int(request.POST.get('clusters'))
	name=(request.POST.get('nameselect'))

	if dataset=='IMDB - Ratings':
	 	settype="ratings"
	 	
	 	initrows=Movies_all.values_list('rating_count','rating','title').exclude(rating_count__gte=100).exclude(rating_count__lt=1)[:numres]
	 	
	 	rows=[]
	 	for i,e in enumerate(initrows):
	 		x=(e[1]*10)

	 		rows.append((e[0],int(x),e[2]))

	elif dataset=='IMDB - Actors':
		settype="actors"
	 		
		#rows=Actors_all.values_list('movie_ref','movie_ref__rating','fullname')

		initrows=Actors.objects.count_avg()
		rows = []
		for i,e in enumerate(initrows):
			x=(e[0]*10)
			rows.append((int(x),e[1],e[2]))

	elif dataset=='Iris':
	 	settype="iris"
	 	rows=Iris_all.values_list('sepal_width','petal_length','species')[:numres]
	elif dataset=='Blobs':
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
		'clusters':klust,
		'name':name
		
		})
	
	return render(request, 'scatterchart.html',context) 