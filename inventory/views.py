from django.shortcuts import render
from django.http import HttpResponse
from .models import Parts
# Create your views here.

def Home(reqeust):
    allparts = Parts.objects.all()
    context = {'allparts':allparts}
    
    #return HttpResponse('<h1>Hello Python beginer</h1>')
    return render(reqeust,'inventory/home.html',context)

