from django.shortcuts import render

from .models import *


# Create your views here.

def list(request):
    heros = HeroInfo.objects.all()
    books = BookInfo.objects.all()
    context = {'heros':heros,'books':books}
    return render(request , 'booktest/list.html' , context)