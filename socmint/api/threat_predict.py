import spacy
from sklearn import svm
import numpy as np
import joblib
# Load the saved model
nlp = spacy.load("en_core_web_trf")
clf_svm = joblib.load('svm_model.pkl')
print("Model loaded from svm_model.pkl")

def get_doc_vector(doc):
    token_vectors = np.array([token.vector for token in doc if token.has_vector])
    if token_vectors.size == 0:
        return np.zeros((768,))
    return np.mean(token_vectors, axis=0)

# Example test data
def testing_model():
    test_x = ["I found a suspicious package outside."]
    docs = [nlp(text) for text in test_x]
    test_x_vectors = np.array([get_doc_vector(doc) for doc in docs])
    # Predict using the loaded model
    predictions = clf_svm.predict(test_x_vectors)
    print("Predictions:", predictions)


def testing_model(test_x):
    docs = [nlp(test_x)]
    test_x_vectors = np.array([get_doc_vector(doc) for doc in docs])
    # Predict using the loaded model
    predictions = clf_svm.predict(test_x_vectors)
    return predictions

print("Predictions:", testing_model("I found a suspicious package outside."))



