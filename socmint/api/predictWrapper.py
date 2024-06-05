from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


# Use predict(string) to get output as tensor
def predict (text):
    # Load the model and tokenizer
    model_name = "Kaviel-threat-text-classifier/"
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
def predictBin(text):
    tensor=predict(text)
    values = tensor[0]
    max_index = torch.argmax(values).item()
    return max_index < 5

#Running test inputs
test_positive="I am going to bomb the university"
test_negative="I am in a good mood today"
print("Positive test result : ",predictBin(test_positive))
print("Negative test result : ",predictBin(test_negative))