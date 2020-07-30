from django.shortcuts import render,redirect
from firstapp.models import Student
# Create your views here.
from firstapp.forms import StudentForm

def show(request):
    data=Student.objects.all()
    return render(request,'firstapp/home.html',{'data':data})
def our_form(request):
    form =StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            marks=request.POST.get('marks')
            email=request.POST.get('email')
            Student.objects.create(name=name,marks=marks,email=email)
            print(form.cleaned_data['name'])
            print("basic validations complete")
            return redirect('/a')
    return render(request,"firstapp/form.html",{'form':form})