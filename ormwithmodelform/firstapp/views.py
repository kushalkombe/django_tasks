from django.shortcuts import render,HttpResponseRedirect,redirect
from django.forms import
from firstapp.models import Language,Framework
# Create your views here.
def display_view(request):
    L=Language.objects.all()
    return render(request,'firstapp/display.html',{'L':L})

def add(request,id):
    obj=Language.objects.get(pk=id)
    if request.method=="POST":
        form=frameworkset(request.POST,instance=obj)

        if form.is_valid():
            form.save()
            return redirect('/display/',id=obj.id)
    return render(request,'firstapp/add.html',{'form':form,'obj':obj})



