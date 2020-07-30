from django.shortcuts import render
from django.views import View
from appone.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from appone.utils import is_correctusername
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    messages.success(request,'Authenticated successfully')
                else:
                    messages.error(request,'Disabled account')
            else:
                user=is_correctusername(cd["username"])
                username=cd['username']
                if not user:
                    messages.error(request,'Invalid username')
                else:
                    count=request.session.get(username,0)
                    newcount=count+1
                    request.session[username]=newcount
                    if newcount>=3:
                        user.is_active=False
                        user.save()
                        email=user.email
                        print(email)
                        send_mail('Security alert ','your account has been locked ','from@example.com',['to@example.com'],fail_silently=False,)
                        messages.error(request,'userblocked')
                    if newcount<=3:messages.error(request,f'Invalid login attempt remaining :{3-newcount}')

        return render(request,"dashboard.html")




def logout_view(request):
    logout(request)
    return render(request,"dashboard.html")
