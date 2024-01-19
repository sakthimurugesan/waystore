from django.http import HttpResponse,request
from django.shortcuts import render

def home(request):
    return render(request,'index.html')