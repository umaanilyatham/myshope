from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from flask import request
from .models import things

# Create your views here.

def home(request):
     if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        quanity=request.POST.get('quanity')
        things.objects.create(name=name,price=price,quanity=quanity)
     Things=things.objects.all()
     return render(request,'myshope/things.html',{'Things':Things})
        