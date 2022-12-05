from django.http import HttpResponse
from django.shortcuts import render
from . models import Product

def index(request):
    item=Product.objects.all()
    return render(request, 'index.html',{'items':item})

def contact(request):
    return render(request, 'contact.html')
def one(request):
    return HttpResponse("Hello one")        

