from django.shortcuts import render,HttpResponseRedirect,redirect
def user_login(function):
    def wrap(request,*args,**kwargs):
        if user_login not in request.session:
            return redirect('/userapp/user_login/')
        else:
            function(request,*args,**kwargs)
    return wrap

