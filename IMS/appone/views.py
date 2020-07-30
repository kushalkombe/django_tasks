from django.shortcuts import render,redirect
from appone.models import *
from django.views.generic import *

# Create your views here.
def home_view(request):
    return render(request,'appone/index.html')

def login_view(request):
    return render(request,'appone/login.html')

def r_view(request):
    return render(request,'appone/register.html')

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'

def student_login(request):
    if request.method=="POST":
        username=request.POST.get('suname')
        password=request.POST.get('spassword')
        try:
            user=Student.objects.get(suname=username, spassword=password)
            if user is not None:
                request.session['student']=user.suname
                return redirect('courselist')
            else:
                messages.error(request,'Invalid username and password')
        except Student.DoesNotExist:
            print('Username Does Not Exist')
    return render(request,'appone/login.html')

def student_logout(request):
    try:
        del request.session['student']
    except KeyError:
        pass
    return render(request,'appone/login.html')



class CourseList(ListView):
    model=Course

class CourseDetail(DetailView):
    model=Course

class batchList(ListView):
    model=Batch

class batchDetail(DetailView):
    model=Batch

class facultyList(ListView):
    model=Faculty

class facultyDetail(DetailView):
    model=Faculty
