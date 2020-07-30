from django.shortcuts import render,HttpResponseRedirect
from student_reg_system.forms import StudentRegistrationform
from firstapp.models import Student
# Create your views here.

def view(request):
    if request.method=='POST':
        s=StudentRegistrationform(request.POST)
        if s.is_valid():
            s.save()
        return HttpResponseRedirect("/form/")
    else:
        s=StudentRegistrationform()
    return render(request,'firstapp/form.html',{'s':s})

def show(request):
    s=Student.objects.all()
    return render(request,'firstapp/show.html',{'s':s})

def delete(request,id):
    obj=Student.objects.get(pk=id)
    obj.delete()
    return HttpResponseRedirect('/show/')

def updatedata(request,id):
    obj=Student.objects.get(pk=id)
    f=StudentRegistrationform(instance=obj)
    if request.method=="POST":
        obj.srollno=request.POST['srollno']
        obj.sname=request.POST['sname']
        obj.smarks=request.POST['smarks']
        obj.saddr=request.POST['saddr']
        obj.save()
        # obj.update(srollno=request.POST['srollno'],sname=request.POST['sname'],smarks=request.POST['smarks'],saddr=request.POST['saddr'])
        return HttpResponseRedirect('/show/')
    return render(request,'firstapp/update.html',{'obj':obj,'f':f})




