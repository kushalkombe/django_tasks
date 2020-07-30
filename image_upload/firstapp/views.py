from django.shortcuts import render,redirect
from firstapp.models import Summer
from firstapp.forms import SummerForm
# Create your views here.
def show(request):
    obj=Summer.objects.all()
    return render(request,'firstapp/show.html',{'obj':obj})

def form(request):
    obj=SummerForm()
    if(request.method=="POST"):
        obj=SummerForm(request.POST,request.FILES)
        if(obj.is_valid()):
            obj.save()
        return redirect('/show/')
    return  render(request,'firstapp/form.html',{'obj':obj})
