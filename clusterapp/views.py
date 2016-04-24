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

	template = loader.get_template('index.html')
	
	return render(request,'index.html', {})

def details(request):

	template = loader.get_template('details.html')
	if request.method == 'POST':
		form = ClusterForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('cluster-results/')
	else:
		form =ClusterForm()	
	return render(request,'details.html', {'form': form})	


def pured3(request):
	dataset=(request.POST.get('dataset'))
	algorithm=(request.POST.get('algorithm'))
	clust=(request.POST.get('clusters'))
	numres=(request.POST.get('numresults'))
	#name=(request.POST.get('nameselect'))
	
	dataset=='IMDB - Ratings'
 	settype="ratings"
 	
 	initrows=Movies_all.values_list('rating_count','rating','title').exclude(rating_count__gte=100).exclude(rating_count__lt=1)[:numres]
 	
 	rows=[]
 	for i,e in enumerate(initrows):
 		x=(e[1]*10)

 		rows.append((e[0],int(x),e[2]))
		
	# 	return rows
	# return rows
	# elif dataset=='IMDB - Actors':
	# 	settype="actors"

	# 	initrows=Actors.objects.count_avg()
	# 	rows = []
	# 	for i,e in enumerate(initrows):
	# 		x=(e[0]*10)
	# 		rows.append((int(x),e[1],e[2]))
	

	klust = int(clust)
	clusted=k_means(rows,k=klust)		



	##Context takes two variables - a dictionary mapping var names to var vals
	##These vars are made available on scatter page
	
	context = RequestContext(request, {
		'data': json.dumps(clusted),
		'settype': json.dumps(settype), 
		'dataset':dataset,
		'clusters':klust,
		#'name':name
		
		})
	
	return render(request, 'scatterchart.html',context) 