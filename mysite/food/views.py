from django.shortcuts import render
from django.http import HttpResponse
from food.models import item

# Create your views here.

def index(request):
    itemlist= item.objects.all()
    context={
        'itemlist':itemlist
    }
    return render(request, 'food/index.html',context)
def detail(request):
    return HttpResponse('<h1 style="color:blue">This is an details view</h1>')
