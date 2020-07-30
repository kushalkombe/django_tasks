from django.shortcuts import render
from testapp.models import Beer
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
# Create your views here.

class BeerListView(ListView):
    model=Beer

class BeerDetailView(DetailView):
    model=Beer

class BeerView(CreateView):
    model=Beer
    fields='__all__'
    success_url = reverse_lazy('beer')

class BeerUpadteView(UpdateView):
    model=Beer
    fields='__all__'

class BeerDeleteView(DeleteView):
    model=Beer
    success_url = reverse_lazy('beer')
