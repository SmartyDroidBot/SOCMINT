from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from api.reddit_api import fetch_hot_posts, search_posts, fetch_post_details
from api.predictWrapper import predict,predictBin

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