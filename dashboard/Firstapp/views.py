from django.shortcuts import render,redirect
from .models import ITJobs,MECHJobs,CIVILJobs
from .forms import ITJobForms,MECHJobForms,CIVILJobForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# Admin dashboard
@login_required(login_url='/login/')
def dashboard(request):
    return render(request,'dashboard.html')
    
# admin welcome page
def welcome_admin(request):
    return render(request,'Welcome_admin.html')

#Admin IT job show
@login_required(login_url='/login/')
def it_show(request):
    print('itshow')
    obj=ITJobs.objects.all()
    return render(request,'it_show.html',{'obj':obj})

# Admin It jobs add
@login_required(login_url='/login/')
def it_add(request):
    if request.method=='POST':
        itform=ITJobForms(request.POST)
        if itform.is_valid():
            itform.save()
        return redirect('/firstapp/it_show/')

    itform=ITJobForms()
    return render(request,'it_add.html',{'itform':itform})

# Admin IT jobs delete
@login_required(login_url='/login/')
def it_delete(request,id):
    obj=ITJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/firstapp/it_show/')

# Admin IT jobs update
@login_required(login_url='/login/')
def it_update(request,id):
    obj=ITJobs.objects.get(pk=id)
    itforms=ITJobForms(instance=obj)
    if(request.method=='POST'):
        itforms=ITJobForms(request.POST,instance=obj)
        if itforms.is_valid():
            itforms.save()
        return redirect('/firstapp/it_show/')
    return render(request,'it_update.html',{'itforms':itforms,'obj':obj})

#*** Mechanical job

# Admin Mech job show
@login_required(login_url='/login/')
def mech_show(request):
    obj=MECHJobs.objects.all()
    return render(request,'mech_show.html',{'obj':obj})

# Admin Mech Job add
@login_required(login_url='/login/')
def mech_add(request):
    if request.method=='POST':
        mechform=MECHJobForms(request.POST)
        if mechform.is_valid():
            mechform.save()
        return redirect('/firstapp/mech_show/')

    mechform=MECHJobForms()
    return render(request,'mech_add.html',{'mechform':mechform})

# Admin Mech job delete
@login_required(login_url='/login/')
def mech_delete(request,id):
    obj=MECHJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/firstapp/mech_show/')

# Admin Mech job update
@login_required(login_url='/login/')
def mech_update(request,id):
    obj=MECHJobs.objects.get(pk=id)
    mechforms=MECHJobForms(instance=obj)
    if(request.method=='POST'):
        mechforms=MECHJobForms(request.POST,instance=obj)
        if mechforms.is_valid():
            mechforms.save()
        return redirect('/firstapp/mech_show/')
    return render(request,'mech_update.html',{'mechforms':mechforms,'obj':obj})

# *** CIVIL JOB

#Admin civil job show
@login_required(login_url='/login/')
def civil_show(request):
    obj=CIVILJobs.objects.all()
    return render(request,'civil_show.html',{'obj':obj})

# Admin civil job add
@login_required(login_url='/login/')
def civil_add(request):
    if request.method=='POST':
        civilform=CIVILJobForms(request.POST)
        if civilform.is_valid():
            civilform.save()
        return redirect('/firstapp/civil_show/')

    civilform=CIVILJobForms()
    return render(request,'civil_add.html',{'civilform':civilform})

# Admin civil job delete
@login_required(login_url='/login/')
def civil_delete(request,id):
    obj=CIVILJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/firstapp/civil_show/')

#Admin civil job update
@login_required(login_url='/login/')
def civil_update(request,id):
    obj=CIVILJobs.objects.get(pk=id)
    civilforms=CIVILJobForms(instance=obj)
    if(request.method=='POST'):
        civilforms=CIVILJobForms(request.POST,instance=obj)
        if civilforms.is_valid():
            civilforms.save()
        return redirect('/firstapp/civil_show/')
    return render(request,'civil_update.html',{'civilforms':civilforms,'obj':obj})

def showresume(request,id):
    itjob=ITJobs.objects.get(pk=id)
    users=itjob.user_it.all()
    # for user in users:
    #     user_resume=user.Resume
    return render(request,'applyresume.html',{'user_resume':users})

def showMECHresume(request,id):
    mechjob=MECHJobs.objects.get(pk=id)
    users=mechjob.user_mech.all()
    # for user in users:
    #     user_resume=user.Resume
    return render(request,'apply_mech_resume.html',{'user_resume':users})

def showCIVILresume(request,id):
    civiljob=CIVILJobs.objects.get(pk=id)
    users=civiljob.user_civil.all()
    # for user in users:
    #     user_resume=user.Resume
    return render(request,'applyresume.html',{'user_resume':users})


