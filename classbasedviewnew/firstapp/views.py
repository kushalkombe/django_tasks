from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views import View
from firstapp.models import Student
from firstapp.forms import StudentForm
from django.views.generic import ListView
# Create your views here.

class StudentView(ListView):
    model=Student
    template_name='show.html'
    context_object_name='obj'

# class StudentView(View):
#     def get(self,request):
#         obj=Student.objects.all()
#         return render(request,'show.html',{'obj':obj})
#     def post(self,request):
#         return render(request,'show.html')

class StudentAddView(View):
    def get(self,request):
        stdform=StudentForm()
        return render(request,'add.html',{'stdform':stdform})
    def post(self,request):
        stdform=StudentForm(request.POST)
        print(request.POST)
        if (stdform.is_valid()):
            stdform.save()
            return redirect('/show/')
        return render(request,'show.html',{'stdform':stdform})

class StudentUpdateView(View):
    form=StudentForm
    def get(self,request,id):
        obj=Student.objects.get(pk=id)
        f=self.form(instance=obj)
        return render(request,'update.html',{'obj':obj,'Form':f})

    def post(self,request,id):
        obj=Student.objects.get(pk=id)
        std=self.form(request.POST,instance=obj)
        print(std)
        if std.is_valid():
            std.save()
            return redirect('/show/')

        return render(request,'update.html',{'obj':obj,'form':std})

class StudentDeleteView(View):
    def get(self,request,id):
        obj=Student.objects.get(pk=id)
        obj.delete()
        return redirect("/show/")



