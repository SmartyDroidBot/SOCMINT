from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def home(request):
    return render(request,'root/home.html')

def twitter(request):
    return render(request,'root/twitter.html')

def reddit(request):
    return render(request,'root/reddit.html')