from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from predictWrapper import predict,predictBin
from reddit_api import initialize,fetch_post_details

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
x=filter_malicous_keywords({'I created a table of volume-friendly snacks to help me choose snacks': '1911fpm'})
print(x)
y=filter_malicous_keywords({'If anyone has already done this I will send Thomas the thermonuclear bomb after them': 'c62pwu'})
print(y)