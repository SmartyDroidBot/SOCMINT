import os
import praw
from dotenv import load_dotenv
from collections import defaultdict
from .predictWrapper import predict
from prawcore.exceptions import BadRequest

# Load environment variables
load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )

def split_text(text, max_length=512):
    words = text.split()
    chunks = []
    chunk = []

    for word in words:
        if len(" ".join(chunk + [word])) <= max_length:
            chunk.append(word)
        else:
            chunks.append(" ".join(chunk))
            chunk = [word]

    if chunk:
        chunks.append(" ".join(chunk))
    
    return chunks

def process_reddit_search(keywords, subreddit, limit, comment_limit, search_comments, check_descriptions):
    reddit = get_reddit_instance()
    query = keywords

    # Preprocess subreddit string
    if subreddit and not subreddit.startswith('r/'):
        subreddit = f'r/{subreddit}'

    print(f"Searching subreddit: {subreddit}, Query: {query}")  # Debugging line

    try:
        submissions = reddit.subreddit(subreddit[2:] if subreddit else 'all').search(query, limit=100)
    except BadRequest as e:
        print("BadRequest:", e.response.text)
        return []  # Return empty list if there's a bad request

    results = []
    for submission in submissions:
        post_data = {
            'title': submission.title,
            'description': submission.selftext,
            'url': submission.url,
            'subreddit': submission.subreddit.display_name
        }
        text = submission.title
        if check_descriptions:
            text += " " + submission.selftext
        
        comments = ""
        if search_comments:
            submission.comments.replace_more(limit=0)
            top_comments = submission.comments.list()[:comment_limit]
            for comment in top_comments:
                comments += comment.body + " "
        
        full_text = text + " " + comments
        print(f"Title and Description: {text}")  # Debugging line
        print(f"Comments: {comments}")  # Debugging line

        # Predict title + description
        title_prediction = predict(submission.title)
        labels = [
            "Banking Fraud",
            "Terrorist Attack",
            "Life Threat",
            "Online Scams",
            "Information Leakage",
            "Casual Conversation"
        ]
        label_index = title_prediction.argmax().item()
        label = labels[label_index]

        # Omit Casual Conversation results
        if label != "Casual Conversation":
            accuracy = title_prediction[0][label_index].item()
            post_data['label'] = label
            post_data['accuracy'] = accuracy*100
        
            if check_descriptions:
                description_chunks = split_text(submission.selftext)
                description_labels = []
                for chunk in description_chunks:
                    prediction = predict(chunk)
                    label_index = prediction.argmax().item()
                    label = labels[label_index]
                    description_labels.append(label)
                    if label != "Casual Conversation":
                        post_data['description_label'] = label
        
            if search_comments:
                comment_chunks = split_text(comments)
                comment_labels = []
                for chunk in comment_chunks:
                    prediction = predict(chunk)
                    label_index = prediction.argmax().item()
                    label = labels[label_index]
                    comment_labels.append(label)
                    if label != "Casual Conversation":
                        post_data.setdefault('comment_labels', []).append(label)
            
            results.append(post_data)
        
        if len(results) >= limit:
            break

    return results[:limit]
