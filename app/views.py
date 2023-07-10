from django.shortcuts import render
from app.models import *
from django.db.models import Q
# Create your views here.

def display_topics(request):
    LTO=Topic.objects.all()
    
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_Webpages(request):
    LWO=Webpage.objects.all()
    
    d={'LWO':LWO}
    return render(request,'display_Webpages.html',d)

def display_AccessRecord(request):
    LAO=AccessRecord.objects.all()
    LAO=AccessRecord.objects.filter(date__gt='1931-10-23')
    LAO=AccessRecord.objects.filter(date__lt='2020-06-14')
    LAO=AccessRecord.objects.filter(date__gte='1931-10-23')
    LAO=AccessRecord.objects.filter(date__lte='2020-06-14')
    LAO=AccessRecord.objects.filter(date__year='2020')
    LAO=AccessRecord.objects.filter(date__month='10')
    LAO=AccessRecord.objects.filter(date__day='15')
    LAO=AccessRecord.objects.filter(name__in=['dhoni','sunil'])
    d={'LAO':LAO}
    return render(request,'display_AccessRecord.html',d)


def Update_Webpage(request):
    LWO=Webpage.objects.all()
    Webpage.objects.filter(name='dhoni').update(url='http://dhoni.com')
    Webpage.objects.filter(name='sunil').update(url='http://sunil.in')
    Webpage.objects.filter(name='ronaldo').update(url='https://ronaldo.in')
    d={'LWO':LWO}
    return render(request,'display_Webpages.html',d)
