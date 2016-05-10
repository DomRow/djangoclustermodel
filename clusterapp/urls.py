from django.conf.urls import include,url,patterns
from django.contrib import admin
import views

#urlpatterns is a route list that redirects URLs to view functions
urlpatterns = patterns('',
    url(r'^$', views.index, name='index.html'),
    #url(r'^$details/', views.details, name='details.html'),
    url(r'^$cluster-results/', views.pured3, name='scatterchart.html'),
)
