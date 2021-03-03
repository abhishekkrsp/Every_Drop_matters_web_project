from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'lifeto/index.html')


def stock(request):
    return render(request,'stock/index.html')

def collect(request):
    return render(request,'doctors/collect.html')

def give(request):
    return render(request,'doctors/give.html')