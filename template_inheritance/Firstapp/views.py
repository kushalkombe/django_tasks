from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='hello everybody very good'
    if h<12:
        msg=msg+'morning'
    elif h<15:
        msg=msg+'afternoon'
    else:
        msg=msg+'night'
    response=render(request,'Firstapp/about.html',{'m':msg,'date':datetime})
    return response
