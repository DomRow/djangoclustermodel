from django.core import serializers
from models import *
from forms import ClusterForm
from tests.testblobs import blob1,rings1,crescent1
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse,Template,Context
from django.shortcuts import render_to_response
from django.db.models import Count
import random, json
import time

def index(request):

	template = loader.get_template('details.html')
	form =ClusterForm()	
	return render(request,'details.html', {'form': form})

def pured3(request):
	dataset=(request.POST.get('dataset'))
	algorithm=(request.POST.get('algorithm'))
	numres=(request.POST.get('numresults'))
	klust=int(request.POST.get('clusters'))
	print (dataset)

	if dataset=='ratings':
	 	settype="ratings"
	 	initrows=Movies_all.values_list('rating_count','rating','title').exclude(rating_count__gte=100).exclude(rating_count__lt=1)[:numres]
	 	rows=[]
	 	for i,e in enumerate(initrows):
	 		x=(e[1]*10)
	 		rows.append((e[0],int(x),e[2]))
	 	
	elif dataset=='iris':
	 	settype="iris"
	 	rows=Iris_all.values_list('sepal_width','petal_length','species')[:numres]
	elif dataset=='year':
	 	settype="year"
	 	rows=Movies_all.values_list('year','rating','title')[:numres] 	
	elif dataset=='blobs':
	 	print blob1
	 	settype="blobs"
		rows=blob1
	elif dataset=='rings':
		settype="rings"
		rows=rings1	
	elif dataset=='crescents':
		settype="crescents"
	 	rows=crescent1
	else: print ('Select')
	
	clusted=k_means(rows,k=klust)

	context = RequestContext(request, {
		'data': json.dumps(clusted),
		'settype': json.dumps(settype), 
		'dataset':dataset,
		'clusters':klust
		})
	
	return render(request, 'scatterchart.html',context)  		
