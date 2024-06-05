import praw
import prawcore
from dotenv import load_dotenv
import os
load_dotenv()

def initialize():
    # Reddit API credentials
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    USER_AGENT = os.getenv("USER_AGENT")

    # Authenticate with Reddit API
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)
    return reddit

# Function to fetch hot posts from a subreddit with error handling
def fetch_hot_posts(subreddit_name, limit=10):
    reddit = initialize()
    try:
        subreddit = reddit.subreddit(subreddit_name)
        posts = {}
        for submission in subreddit.hot(limit=limit):
            posts[submission.title] = submission.id
        return posts
    except prawcore.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return {}
    except prawcore.exceptions.ResponseException as e:
        print(f"ResponseException: {e}")
        return {}
    except prawcore.exceptions.PrawcoreException as e:
        print(f"PrawcoreException: {e}")
        return {}

# Function to search for posts containing a specific keyword across all of Reddit
def search_posts(keyword, limit=10):
    reddit = initialize()
    try:
        # Search for posts in all of Reddit
        search_results = reddit.subreddit('all').search(keyword, limit=limit)
        
        posts = {post.title: post.id for post in search_results}
        return posts
    except prawcore.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return {}
    except prawcore.exceptions.ResponseException as e:
        print(f"ResponseException: {e}")
        return {}
    except prawcore.exceptions.PrawcoreException as e:
        print(f"PrawcoreException: {e}")
        return {}

# Function to fetch and print details of a specific post
def fetch_post_details(post_id):
    reddit = initialize()
    try:
        submission = reddit.submission(id=post_id)
        details = {
            "Title": submission.title,
            "URL": submission.url,
            "Description": submission.selftext,
        }

        # Fetch and add top-level comments to the details (optional)
        submission.comments.replace_more(limit=0)
        comments = []
        for top_level_comment in submission.comments:
            comments.append({
                "Comment Body": top_level_comment.body,
            })
        details["Comments"] = comments

        return details
    except prawcore.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return {}
    except prawcore.exceptions.ResponseException as e:
        print(f"ResponseException: {e}")
        return {}
    except prawcore.exceptions.PrawcoreException as e:
        print(f"PrawcoreException: {e}")
        return {}

if __name__ == '__main__':
    # Example usage of search_posts
    keyword = 'snacks'
    posts = search_posts(keyword, limit=1)
    print("Search Results (Title: ID):")
    print(posts)

    # Example usage of fetch_post_details
    if posts:
        first_post_id = next(iter(posts.values()))
        post_details = fetch_post_details(first_post_id)
        print("\nPost Details:")
        print(post_details)
        print("\nPost URL:")
        print(post_details["URL"])
