from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from firstapp.forms import UserRegistrationForm
# Create your views here.
def user(request):
    if request.method=='POST':
        u=UserRegistrationForm(request.POST)
        if u.is_valid():
            u.save()
    u=UserRegistrationForm()
    return render(request,'firstapp/form.html',{'u':u})

def success(request):
    return render(request,'firstapp/success.html')
