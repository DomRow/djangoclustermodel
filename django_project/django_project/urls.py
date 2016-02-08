
from django.conf.urls import url,patterns
from django.contrib import admin
from djangoApp import views

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index.html'),
  	#url(r'^your-name/',views.get_name,name='name.html'),
  	url(r'^your-name/',views.index,name='the'),
)