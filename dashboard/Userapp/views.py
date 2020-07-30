from django.shortcuts import render,redirect
from Userapp.forms import UserForm,UserProfile
from Firstapp.models import ITJobs,MECHJobs,CIVILJobs
from Userapp.decorator import user_login
from Userapp.models import UserReg
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
# user first welcome page
def welcome_user(request):
    return render(request,'Welcome_user.html')
#dashboard page
def userdashboard(request):
    return render(request,'dashboard_user.html')

# User Registration page
def userregister(request):
    
    if request.method=="POST":
        ureg=UserForm(request.POST,request.FILES)
        if ureg.is_valid():
            ureg.save()
        return redirect('/userapp/user_login/')
    ureg=UserForm()   
    return render(request,'userreg.html',{'ureg':ureg})

def updateprofile(request):
    id=request.session.get('user_id')
    print('user_id',id)
    pobj=UserReg.objects.get(pk=id)
    print('update profile',pobj)
    pforms=UserForm(instance=pobj)
    print(pforms)
    if(request.method=='POST'):
        pforms=UserProfile(request.POST,request.FILES,instance=pobj)
        if pforms.is_valid():
            pforms.save()
        return redirect('/userapp/user_login/')
    pforms=UserProfile(instance=pobj)
    return render(request,'updateprofile.html',{'pforms':pforms})


#User login page
def UserLogin(request,*args,**kwargs):
    if request.method=='POST':
        Username=request.POST['txtuname']
        Password=request.POST["txtpasswd"]
        try:
            user=UserReg.objects.get(Username=Username,Password=Password)
            if (user):
                request.session['user'] = user.Username
                request.session['user_id']=user.id
                print(request.session.get('user'))
                return render(request,'dashboard_user.html')
            else:
                messages.error(request,'please enter valid username and password')
                return redirect('/userapp/user_login/')  
        except Exception :
            messages.error(request,'please enter valid username and password')
            return redirect('/userapp/user_login/')  
    return render(request,'loginuser.html')

#User IT JOB show
@user_login
def it_showuser(request):
    obj=ITJobs.objects.all()
    return render(request,'it_show_user.html',{'obj':obj})

#User Mechanical Job show
@user_login
def mech_showuser(request):
    obj=MECHJobs.objects.all()
    return render(request,'mech_show_user.html',{'obj':obj})
        
#User civil job show
@user_login
def civil_showuser(request):
    obj=CIVILJobs.objects.all()
    return render(request,'civil_show_user.html',{'obj':obj})

@user_login
def apply_user_IT(request,*args,**kwargs):
    jobid = kwargs.get('id')
    if jobid:
        messages.success(request,'You have applied successfully ,we will inform you by mail')
        obj=ITJobs.objects.get(pk=jobid)
        uid=request.session.get('user_id')
        uobj=UserReg.objects.get(pk=uid)
        obj.user_it.add(uobj)
        obj.save()
        return redirect('/userapp/it_show_user/')
    return redirect('/userapp/it_show_user/')

@user_login
def apply_user_MECH(request,*args,**kwargs):
    jobid=kwargs.get('id')
    if jobid:
        messages.success(request,'You have applied successfully ,we will inform you by mail')
        obj=MECHJobs.objects.get(pk=jobid)
        user_id=request.session.get('user_id')
        uobj=UserReg.objects.get(pk=user_id)
        obj.user_mech.add(uobj)
        obj.save()
        return redirect('/userapp/mech_show_user/')
    return redirect('/userapp/mech_show_user/')

@user_login
def apply_user_CIVIL(request,*args,**kwargs):
    jobid=kwargs.get('id')
    if jobid:
        messages.success(request,'You have applied successfully ,we will inform you by mail')
        obj=CIVILJobs.objects.get(pk=jobid)
        user_id=request.session.get('user_id')
        uobj=UserReg.objects.get(pk=user_id)
        obj.user_civil.add(uobj)
        obj.save()
        return redirect('/userapp/civil_show_user/')
    return redirect('/userapp/civil_show_user/')


