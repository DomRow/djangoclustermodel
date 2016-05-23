from django.conf.urls import include,url
from django.contrib import admin
from clusterapp import views

#urlpatterns is a route list that redirects URLs to view functions
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index.html'),
    #url(r'^details/', views.details, name='details.html'),
    url(r'^cluster-results/', views.pured3, name='scatterchart.html'),
    #Comment inserted to test updates facility
]
