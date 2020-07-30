"""discussion_forum1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from postapp import views as v
from userapp import views as v1
from django.views.generic import TemplateView
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addpost/',v.Add_post.as_view()),
    path('showpost/',v.post_title.as_view()),
    path('postdetails/<int:id>/',v.post_details.as_view()),
    path('userreg/',v1.userregister.as_view()),
    path('login/',v1.UserLogin.as_view()),
    path('welcome/', TemplateView.as_view(template_name="welcome1.html")),
    # path('a/',lambda request: render(request,"welcome1.html")),
    # path('userreg/',v1.userregister.as_view()),
    # path('user/',)

]
