from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def endpoint(request):
    
    return HttpResponse('<h1>MODULO 2!!!!</h1>')