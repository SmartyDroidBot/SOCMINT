from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def home(request):
    return render(request,'home.html')
def twitter(request):
    return render(request,'twitter.html')
def reddit(request):
    return render(request,'reddit.html')
def telegram(request):
    return render(request,'telegram.html')
def instagram(request):
    return render(request,'instagram.html')