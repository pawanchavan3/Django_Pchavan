from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1 style="color:black">This is an index views</h1>')

def detail(request):
    return HttpResponse('<h1 style="color:blue">This is an details</h1>')