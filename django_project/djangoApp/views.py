from django.core import serializers
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.template.response import TemplateResponse,Template,Context
from models import Director,Actors,Movies, Iris,Genres,kmeans,norm
from .forms import NameForm, MovieForm
from django_project import wsgi
from django.shortcuts import render_to_response
import random,datetime,time


from blobs import blob1,blob2,crescent1,crescent2,circle1,circle2
import json 

Moviesall=Movies.objects.all()

Irisall=Iris.objects.all()

def index(request):
	result_list = Moviesall.values('rating_count')[:10]
	
	template = loader.get_template('index.html')
	context = {'result_list': result_list,}
	return render(request,'index.html', context)


# def search(request):

# 	rc = Moviesall.values_list('rating_count',flat=True)[:19]
# 	r = Moviesall.values_list('rating',flat=True)[:19]	
# 	#val2 = request.POST.get('getval', None)
	
# 	combo=((((rc[i]),(r[i]))) for i in range(len(rc)))
# 	raj=list(combo)	
# 	print raj
# 	html=raj
	
# 	#context = ({'htmo': htmo,})
# 	#return render(request, 'name.html', context)
# 	return HttpResponse(html)

def blobchart(request):
    #xdataprenorm=blob1
    #ydata1prenorm=Moviesall.values_list('rating',flat=True)[:100]
    xdata=[ [(1,1)], [], [(3.5,5)], [(1.5,2),(3,4),(5,7),(4.5,5),(3.5,4.5)]]
    ydata1=[ [(1,1)], [], [3.5,5], [(1.5,2),(3,4),(5,7),(4.5,5),(3.5,4.5)]]
    
    print xdata,ydata1
    #kmeans(xdata,3)
   
    #ydata1 = [i * random.randint(1, 10) for i in range(nb_element)]
    #ydata2 = map(lambda x: x * 2, ydata1)
    #ydata3 = map(lambda x: x * 5, ydata1)

    kwargs1 = {'shape': 'circle','color':'green'}
    kwargs2 = {'shape': 'cross'}
    #kwargs3 = {'shape': 'triangle-up'}

    extra_serie1 = {"tooltip": {"y_start": "AAA", "y_end": " balls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata1, 'kwargs1': kwargs1, 'extra1': extra_serie1
        #'name2': 'series 2', 'y2': ydata2, 'kwargs2': kwargs2, 'extra2': extra_serie1,
        #'name3': 'series 3', 'y3': ydata3, 'kwargs3': kwargs3, 'extra3': extra_serie1
    }
    charttype = "scatterChart"
    chartcontainer = "scatterchart_container"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        
    }

    return render_to_response('scatterchart.html', data)

def pured3(request):
	dataset=(request.POST.get('getset'))
	algorithm=(request.POST.get('getalg2'))
	numres=(request.POST.get('getnums'))
	klust=int(request.POST.get('getval'))
		
	
	
	#titleslist=Moviesall.values_list('title').exclude(rating_count__gte=100).exclude(rating_count__lt=1)[:300]

	
	
	if dataset=='IMDB - Ratings':
	 	settype="ratings"
	 	rows=Moviesall.values_list('rating_count','rating').exclude(rating_count__gte=100).exclude(rating_count__lt=1)[:300]
	elif dataset=='Iris':
	 	settype="iris"
	 	rows=Irisall.values_list('sepal_width','sepal_length')[:150]
	 	#return xpnorm1
	else: return 0
	
	clusted=kmeans(rows,k=klust)

	##Context takes two variables - a dict mapping var names tovar vals
	##This var is made available then on the chart page
	context = RequestContext(request, {
		'data': json.dumps(clusted),
		#'titles': json.dumps(title),
		'settype': json.dumps(settype), 
		'dataset':request.POST.get('getset'),
		'kclusters':request.POST.get('getval')
		})
	
	return render(request, 'scatterchart.html',context)

def irisd3(request):
	xpnorm1=Irisall.values_list('sepal_width','sepal_length')[:100]
	klust=int(request.POST.get('getval'))
	clusted=kmeans(xpnorm1,k=klust)
	rRc=json.dumps(clusted)
	print rRc
	context = RequestContext(request, {
		'rating': rRc,
		'dataset':request.POST.get('getset'),
		'kclusters':request.POST.get('getval')
		})
	
	return render(request, 'scatterchart.html',context)