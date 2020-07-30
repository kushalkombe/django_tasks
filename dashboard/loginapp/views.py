from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

def welcome(request):
    return render(request,'Welcome1.html')

def register(request):
    if request.method=='POST':
        obj=UserCreationForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/login/')
    obj=UserCreationForm()
    return render(request,'register.html',{'obj':obj})
