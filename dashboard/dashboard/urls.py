from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', include('Firstapp.urls')),
    path('userapp/', include('Userapp.urls')),
    path('', include('loginapp.urls')),
    path('login/',auth_view.LoginView.as_view(template_name='login.html')),
    path('logout/',auth_view.LogoutView.as_view()),
    path('api/', include('Firstapp.api.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
