# socmint/api/reddit_api.py

import os
import praw
from dotenv import load_dotenv
from collections import defaultdict
from .predictWrapper import predict

# Load environment variables
load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )

# socmint/api/reddit_api.py

from prawcore.exceptions import BadRequest

def process_reddit_search(keywords, subreddit, limit, search_comments):
    reddit = get_reddit_instance()
    query = keywords

    # Preprocess subreddit string
    if subreddit and not subreddit.startswith('r/'):
        subreddit = f'r/{subreddit}'

    print(f"Searching subreddit: {subreddit}, Query: {query}")  # Add this line for debugging

    if subreddit:
        try:
            submissions = reddit.subreddit(subreddit).search(query, limit=limit)
        except BadRequest as e:
            print("BadRequest:", e.response.text)
            return []  # Return empty list if there's a bad request
    else:
        submissions = reddit.subreddit('all').search(query, limit=limit)

    results = []
    for submission in submissions:
        post_data = {
            'title': submission.title,
            'description': submission.selftext,
            'url': submission.url,
            'subreddit': submission.subreddit.display_name
        }
        text = submission.title + " " + submission.selftext
        comments = ""
        if search_comments:
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comments += comment.body + " "
            text += " " + comments
        print(submission.title)

        prediction = predict(text)
        labels = [
            "Banking Fraud",
            "Terrorist Attack",
            "Life Threat",
            "Online Scams",
            "Information Leakage",
            "Casual Conversation"
        ]
        label_index = prediction.argmax().item()
        label = labels[label_index]
        
        # Omit Casual Conversation results
        if label != "Casual Conversation":
            accuracy = prediction[0][label_index].item()
            post_data['label'] = label
            post_data['accuracy'] = accuracy
            if search_comments:
                post_data['comments'] = comments

            results.append(post_data)
    
    return results
