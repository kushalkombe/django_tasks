from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from firstapp.models import Products ,Category
from firstapp.forms import ProductForm

def sign_up(request):
    context = {}
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    context['form']=form
    return render(request,'sign_up.html',context)

class Productview(View):
    def get(self,request):
        obj1 =Products.objects.all()
        return render(request,'show.html',{'obj':obj1})

class AddProdView(View):
    def get(self,request):
        obj=ProductForm()
        return render(request,'add.html',{'obj':obj})

    def post(self,request):
        obj=ProductForm(request.POST ,files=request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('/prod_view/')



def prod_update(request,id):
    obj=Products.objects.get(pk=id)
    pforms=ProductForm(instance=obj)
    if(request.method=='POST'):
        pforms=ProductForm(request.POST,instance=obj,files=request.FILES)
        if pforms.is_valid():
            pforms.save()
        return redirect('/prod_view/')
    return render(request,'updateproduct.html',{'pforms':pforms,'obj':obj})

def prod_delete(request,id):
    obj=Products.objects.get(pk=id)
    obj.delete()
    return redirect('/prod_view/')


