from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from firstapp.models import *
from firstapp.forms import *
from django.shortcuts import redirect

# Create your views here.

class Studentview(View):
    def get(self,request):
        obj=Student.objects.all()
        return render(request,'firstapp/show.html',{'obj':obj})


class AddStudentView(View):
    def get(self,request):
        studentform=StudentForm()
        return render(request,'firstapp/add.html',{'studentform':studentform})

    def  post(self,request):
        studentform=StudentForm(request.POST)
        if studentform.is_valid():
            studentform.save()
            return redirect('/show/')

class UpdateStudentView(View):
    def get(self,request,id):
        obj=Student.objects.get(pk=id)
        studentform=StudentForm(instance=obj)
        return render(request,'firstapp/update.html',{'studentform':studentform,'obj':obj})
    
    def post(self,request,id):
        obj=Student.objects.get(pk=id)
        studentform=StudentForm(request.POST,instance=obj)
        if studentform.is_valid():
            studentform.save()
            return redirect('/show/')

class DeleteView(View):
    def get(self,request,id):
        obj=Student.objects.get(pk=id)
        obj.delete()
        return redirect('/show/')

  

