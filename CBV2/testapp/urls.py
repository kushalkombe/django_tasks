from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beer/',views.BeerListView.as_view(),name='beer'),
    path('details/<slug:pk>/',views.BeerDetailView.as_view(),name='details'),
    path('create/',views.BeerView.as_view(),name='create'),
    path('update/<slug:pk>/',views. BeerUpadteView.as_view(),name='update'),
    path('delete/<slug:pk>/',views.BeerDeleteView.as_view(),name='delete'),
]
