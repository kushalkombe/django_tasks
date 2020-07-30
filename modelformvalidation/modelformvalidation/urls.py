from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from firstapp import views
from django.contrib import admin



urlpatterns = [
	path('', views.home, name ='index'),
    path('admin/', admin.site.urls),

]
