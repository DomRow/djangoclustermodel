
from django.conf.urls import url,patterns
from django.contrib import admin
from djangoApp import views

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index.html'),
  	#url(r'^your-name/',views.get_name,name='name.html'),
  	url(r'^your-name/',views.demochart2,name='the'),
  	#url(r'^piechart/',views.demochart,name='demo_piechart'),
  	#url(r'^your-name/',views.get_name,name='name.html'),
	#url(r'^pyjama/',views.pyj,name='pyjama.html'),
  	#url(r'^index/',index)
)