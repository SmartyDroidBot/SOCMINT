from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

# Use predict(string) to get output as tensor
def predict(text):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_name = os.path.join(current_dir, "Kaviel-threat-text-classifier")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Check if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Move model to GPU if available
    model.to(device)

    # Tokenize and prepare input
    inputs = tokenizer(text, return_tensors="pt")

    # Move input tensors to the same device as the model
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Get model predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Process outputs (assuming binary classification)
    logits = outputs.logits
    predictions = torch.sigmoid(logits)

    # Return predictions
    return predictions
