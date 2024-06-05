from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from api.reddit_api import fetch_hot_posts, search_posts, fetch_post_details
from api.predictWrapper import predict,predictBin
#from api.filter_predict import filter_malicous_keywords

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

def reddit_api_view(request):
    subreddit_name = request.GET.get('subreddit_name', None)
    keyword = request.GET.get('keyword', None)
    post_id = request.GET.get('post_id', None)
    
    data = {}

    if subreddit_name:
        data['hot_posts'] = fetch_hot_posts(subreddit_name)
    
    if keyword:
        data['search_results'] = search_posts(keyword)
        y=predictBin("hello")
        #data['search_results']=filter_malicous_keywords(data['search_results'])
    
    if post_id:
        data['post_details'] = fetch_post_details(post_id)

    return JsonResponse(data)