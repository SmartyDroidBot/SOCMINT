from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from api.reddit_api import process_reddit_search
from api.predictWrapper import predict
from collections import defaultdict
import re

def sanitize_input(input_str):
    return re.sub(r'[^\w\s]', '', input_str)

def home(request):
    return render(request, 'home.html')

def reddit(request):
    if request.method == 'POST':
        keywords = sanitize_input(request.POST.get('keywords'))
        subreddit = sanitize_input(request.POST.get('subreddit'))
        limit = int(request.POST.get('limit', 10))
        comment_limit = int(request.POST.get('comment_limit', 10))
        search_comments = request.POST.get('search_comments') == 'on'
        check_descriptions = request.POST.get('check_descriptions') == 'on'

        results = process_reddit_search(keywords, subreddit, limit, comment_limit, search_comments, check_descriptions)

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
            if 'description_label' in result:
                descriptions_data[result['description_label']] += 1
            if 'comment_labels' in result:
                for label in result['comment_labels']:
                    comments_data[label] += 1

        context = {
            'results': results,
            'titles_data': [titles_data[label] for label in labels],
            'descriptions_data': [descriptions_data[label] for label in labels],
            'comments_data': [comments_data[label] for label in labels] if search_comments else [],
            'no_results': len(results) == 0
        }

        return render(request, 'reddit_results.html', context)
    
    return render(request, 'reddit.html')
    if request.method == 'POST':
        keywords = sanitize_input(request.POST.get('keywords'))
        subreddit = sanitize_input(request.POST.get('subreddit'))
        limit = int(request.POST.get('limit', 10))
        comment_limit = int(request.POST.get('comment_limit', 10))
        search_comments = request.POST.get('search_comments') == 'on'
        check_descriptions = request.POST.get('check_descriptions') == 'on'

        results = process_reddit_search(keywords, subreddit, limit, comment_limit, search_comments, check_descriptions)

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
            if 'description_label' in result:
                descriptions_data[result['description_label']] += 1
            if 'comment_labels' in result:
                for label in result['comment_labels']:
                    comments_data[label] += 1

        context = {
            'results': results,
            'titles_data': [titles_data[label] for label in labels],
            'descriptions_data': [descriptions_data[label] for label in labels],
            'comments_data': [comments_data[label] for label in labels] if search_comments else [],
            'no_results': len(results) == 0
        }

        return render(request, 'reddit_results.html', context)
    
    return render(request, 'reddit.html')


def twitter(request):
    return render(request, 'twitter.html')

def telegram(request):
    return render(request, 'telegram.html')

def instagram(request):
    return render(request, 'instagram.html')
