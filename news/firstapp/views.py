from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'firstapp/home.html')

def pune_news_view(request):
    news1='pune it sector grows by 3.88 percent'
    news2='pune raining since last two days'
    my_dict={'news1':news1,'news2':news2}
    return render(request,'firstapp/pnews.html',my_dict)

def mumbai_news_view(request):
    news1='ambani hiked jio calling price'
    news2='mumbai raining since last two days'
    my_dict={'news1':news1,'news2':news2}
    return render(request,'firstapp/mnews.html',my_dict)
