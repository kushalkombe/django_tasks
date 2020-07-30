from django.shortcuts import render,HttpResponseRedirect,redirect
def user_login(function):
    def wrap(request,*args,**kwargs):
        if  request.session.get('user') :
            print(request.session.get('user',None))
            return function(request,*args,**kwargs)
        else:
            return redirect('/userapp/user_login/')
    return wrap

