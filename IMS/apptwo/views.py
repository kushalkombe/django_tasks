from django.shortcuts import render
from appone.models import *
from django.views.generic import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

def admin_courseview(request):
    obj=Course.objects.all()
    return render(request,'apptwo/courseview.html',{'obj':obj})

def admin_batchview(request):
    obj=Batch.objects.all()
    return render(request,'apptwo/batchview.html',{'obj':obj})

def admin_facultyview(request):
    obj=Faculty.objects.all()
    # print(request.POST,'***********************')
    # obj1 = Course.objects.filter(faculty__cname = request.POST.get('cname'))
    return render(request,'apptwo/facultyview.html',{'obj':obj})



class CourseCreate(CreateView):
    model = Course
    fields='__all__'
class BatchCreate(CreateView):
    model = Batch
    fields='__all__'
class FacultyCreate(CreateView):
    model = Faculty
    fields='__all__'


class CourseUpdate(UpdateView):
    model = Course
    fields='__all__'
    template_name_suffix = '_update_form'

class BatchUpdate(UpdateView):
    model = Batch
    fields='__all__'
    template_name_suffix = '_update_form'

class FacultyUpdate(UpdateView):
    model = Faculty
    fields='__all__'
    template_name_suffix = '_update_form'


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy("course")

class BatchDelete(DeleteView):
    model = Batch
    success_url = reverse_lazy("batch")

class FacultyDelete(DeleteView):
    model = Faculty
    success_url = reverse_lazy("faculty")
