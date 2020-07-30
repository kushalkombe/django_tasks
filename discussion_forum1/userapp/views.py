from django.shortcuts import render,redirect
from userapp.models import User
from userapp.forms import UserRegForm,LoginForm
from django.views import View
import hashlib

# Create your views here.
def make_password(password):
    assert password
    hash1=hashlib.md5(password.encode(encoding="utf-8")).hexdigest()
    return hash1

class userregister(View):
    def get(self,request):
        form=UserRegForm()
        return render(request,'userreg.html',{'form':form})
    def post(self,request):
        form=UserRegForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            cpassword=form.cleaned_data['confirm_password']
            if (password==cpassword):
                password=make_password(password)
                cpassword=make_password(cpassword)
                user=User()
                user.name=form.cleaned_data['name']
                user.username=form.cleaned_data['username']
                user.password=password
                user.confirm_password=cpassword
                user.email=form.cleaned_data['email']
                print(user.email)
                user.gender=form.cleaned_data['gender']
                user.tags=form.cleaned_data['tags']
                user.save()
                return redirect('/login/')
            else:
                return render(request, 'userruserreg.html', {'form': form})
        else:
            return (request,'userreg.html',{'form':form})


class UserLogin(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'User/userlogin.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            password=make_password()
            user=User.objects.get(username=username,password=password)
            if user is not None:
                request.session['uid']=user.id
                return redirect ('/showpost/')
            else:
                messages.error(request,'please enter valid username and password')
                return redirect('/login/')
        else:
            messages.error(request,'please enter valid username and pwd')
            return redirect('/login/')