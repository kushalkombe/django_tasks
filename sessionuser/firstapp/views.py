from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def display(request):
    #obj=User.username
    user=None
    if request.session.has_key('user'):
        a=request.session.get('user')
        # del request.session['a']
        if a:
            print(a)
            return render(request,'display.html',{'a':a})
        else:
            return redirect('/login/')

def login(request):
    if request.session.has_key('user'):
        return redirect('/display/')
    if (request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        try:
            user=auth.authenticate(username=username,password=password)
            if (user is not None):
                auth.login(request,user)
                request.session['user']='ssssS'
                return render(request,'display.html')
        except (auth.ObjectDoesNotExist):
            print('invalid user')
    return render(request,'login.html')
