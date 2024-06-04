import spacy
import joblib
import numpy as np

# Load the transformer-based spaCy model and the trained SVM model
nlp = spacy.load("en_core_web_trf")
clf_svm = joblib.load('svm_model.pkl')

# Function to get average token vectors for a document
def get_doc_vector(doc):
    token_vectors = np.array([token.vector for token in doc if token.has_vector])
    if token_vectors.size == 0:
        return np.zeros((768,))
    return np.mean(token_vectors, axis=0)

# Wrapper function to predict if the input string is a threat
def predict_threat(text):
    doc = nlp(text)
    vector = get_doc_vector(doc).reshape(1, -1)
    prediction = clf_svm.predict(vector)
    return 1 if prediction[0] == "THREAT" else 0

# Example usage
if __name__ == "__main__":
    example_text = "I found a suspicious package outside."
    print(f"Prediction for '{example_text}': {predict_threat(example_text)}")
