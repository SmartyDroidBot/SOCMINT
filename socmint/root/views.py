from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from api.reddit_api import fetch_hot_posts, search_posts, fetch_post_details
from api.predictWrapper import predict,predictBin

# Create your views here.
def filter_malicous_keywords(posts):
    malicous_posts={}
    for post in posts:
        post_id=posts[post]
        details=fetch_post_details(post_id)
        malicous_title=predictBin(details['Title'])
        malicous_comment=False
        if malicous_title==True or malicous_comment==True:
            print("malicous Title detected")
            malicous_posts[post]=posts[post]
            break
        for comment in details["Comments"]:
            mal_com_temp=predictBin(comment["Comment Body"])
            if mal_com_temp==True:
                if comment['Comment Author']=="AutoModerator":
                    continue
                elif comment["Comment Body"]=="[removed]":
                    continue
                else:
                    print(comment)
                    malicous_comment=True
                    break
        if malicous_title==True or malicous_comment==True:
            print("malicous content detected")
            malicous_posts[post]=posts[post]
        else:
            print("no malicous content detected")
    return malicous_posts
    pass

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
        #y=predictBin("hello","./api/Kaviel-threat-text-classifier/")
        data['search_results']=filter_malicous_keywords(data['search_results'])
    
    if post_id:
        data['post_details'] = fetch_post_details(post_id)

    return JsonResponse(data)