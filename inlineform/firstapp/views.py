from django.shortcuts import render,HttpResponseRedirect,redirect
from django.forms import inlineformset_factory
from firstapp.models import Language,Framework
# Create your views here.
def display_view(request):
    L=Language.objects.all()
    return render(request,'firstapp/display.html',{'L':L})

def add(request,id):
    obj=Language.objects.get(pk=id)
    frameworkset=inlineformset_factory(Language,Framework,fields=('fname',),can_delete=False,extra=1,max_num=5)
    if request.method=="POST":
        form=frameworkset(request.POST,instance=obj)

        if form.is_valid():
            form.save()
            return redirect('/display/',id=obj.id)
    form=frameworkset(instance=obj)
    return render(request,'firstapp/add.html',{'form':form,'obj':obj})



