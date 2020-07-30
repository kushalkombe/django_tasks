from django.shortcuts import render,redirect
from commentsapp.models import Comment
from commentapp.forms import commentform
from postapp.models import Post
from Userapp.models import User
# Create your views here.

class Addcomment(View):
    def post(self,request,*args,**kwargs):
        cform=commentform(request.POST)
        id1=kwargs.get('id')
        postobj=Post.objects.get(pk=id1)
        if cform.is_valid():
            comment=Comment()
            userobj=User.objects.get(pk=1)
            comment.commentbox=cform.cleaned_data['commentbox']
            comment.commentforpost=postobj
            comment.commentbyuser=userobj
            if request.FILES:
                comment.cfileupload=cform.cleaned_data['cfileupload']
            comment.save()
        return redirect(f'/post/postdetail/{id1}/')