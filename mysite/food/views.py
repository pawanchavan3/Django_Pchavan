from django.shortcuts import render
from django.http import HttpResponse
from food.models import item

# Create your views here.

def index(request):
    itemlist= item.objects.all()
    return HttpResponse(itemlist)

def detail(request):
    return HttpResponse('<h1 style="color:blue">This is an details view</h1>')
