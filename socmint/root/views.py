# socmint/root/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from api.reddit_api import process_reddit_search
from api.predictWrapper import predict
from collections import defaultdict

def home(request):
    return render(request, 'home.html')

def twitter(request):
    return render(request, 'twitter.html')

def reddit(request):
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        subreddit = request.POST.get('subreddit')
        limit = int(request.POST.get('limit', 10))
        search_comments = request.POST.get('search_comments') == 'on'

        results = process_reddit_search(keywords, subreddit, limit, search_comments)

        labels = [
            "Banking Fraud",
            "Terrorist Attack",
            "Life Threat",
            "Online Scams",
            "Information Leakage",
            "Casual Conversation"
        ]

        titles_data = defaultdict(int)
        descriptions_data = defaultdict(int)
        comments_data = defaultdict(int)

        for result in results:
            titles_data[result['label']] += 1
            descriptions_data[result['label']] += 1
            if 'comments' in result:
                comments_data[result['label']] += 1

        context = {
            'results': results,
            'titles_data': [titles_data[label] for label in labels],
            'descriptions_data': [descriptions_data[label] for label in labels],
            'comments_data': [comments_data[label] for label in labels] if search_comments else []
        }

        return render(request, 'reddit_results.html', context)
    
    return render(request, 'reddit.html')

def telegram(request):
    return render(request, 'telegram.html')

def instagram(request):
    return render(request, 'instagram.html')
