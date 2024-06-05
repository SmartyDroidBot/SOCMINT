from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


# Use predict(string) to get output as tensor
def predict (text,model_name="api/Kaviel-threat-text-classifier/"):
    # Load the model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)


    # Tokenize and prepare input
    inputs = tokenizer(text, return_tensors="pt")

    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Process outputs (assuming binary classification)
    logits = outputs.logits
    predictions = torch.sigmoid(logits)

    # Return predictions
    return predictions

# Use predictBin(String) to get a direct Threat(True) or Not a threat (False) output
def predictBin(text,model_name="api/Kaviel-threat-text-classifier/"):
    tensor=predict(text,model_name)
    values = tensor[0]
    max_index = torch.argmax(values).item()
    return max_index < 5

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
#Running test inputs
test_positive="I am going to bomb the university"
test_negative="I am in a good mood today"
#print("Positive test result : ",predictBin(test_positive))
#print("Negative test result : ",predictBin(test_negative))