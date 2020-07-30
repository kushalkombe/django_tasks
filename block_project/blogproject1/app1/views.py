from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def list_post_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get("page")
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)    
    return render(request,"app1/post_list.html",{'posts':post_list})



def post_detail(request,post):
    print(post)

    post=get_object_or_404(Post,slug=post)
    #obj.body
    #success_url='/home/'

    return render (request,'app1/detail.html',{'posts':post})
