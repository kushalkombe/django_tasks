from django.shortcuts import render,redirect
from postapp.forms import Addpostform
from postapp.models import Post
from django.views import View
from django.views.generic import DetailView
from commentsapp.forms import Commentform


# Create your views here.
##for adding  the post
class Add_post(View):
    def get(self,request):
        pform=Addpostform()
        return render(request,'post.html',{'pform':pform})

    def post(self,request,*args,**kwargs):
        pform=Addpostform(request.POST)
        if (pform.is_valid()):
            post=Post(title=pform.cleaned_data['title'],description=pform.cleaned_data['description'],ptag=pform.cleaned_data['ptag'])
            if (request.FILES):
                post.fileupload=pform.cleaned_data['fileupload']
                uid=request.session.get('uid')
                print(uid)
                user_obj=User.objects.get(pk=uid)
                post=postbyuser=user_obj
                post.save()

            pform.save()
            return redirect('/showpost/')
#for showing the post

class post_title(View):
    def get(self,request):
        obj=Post.objects.all()
        return render(request,'home.html',{'obj':obj})

class post_details(DetailView):
    def get(self,request,id):
        pobj=Post.objects.get(pk=id)
        return render(request,'postdetails.html',{'pobj':pobj})

