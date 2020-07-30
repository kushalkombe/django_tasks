from django.urls import path
from django.contrib.auth import views as auth_views
from appone import views


urlpatterns=[
    path("login/",views.LoginView.as_view()),
    # path("logout/",views.LogoutView.as_view(template_name="registration/logout.html"),name="logut"),
    path("logout/",views.logout_view)
    ]
