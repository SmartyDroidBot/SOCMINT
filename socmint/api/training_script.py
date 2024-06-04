import spacy
from sklearn import svm
import numpy as np
import joblib
import pandas as pd

# Load the transformer-based spaCy model
nlp = spacy.load("en_core_web_trf")

# Define categories
class Category:
    THREAT = "THREAT"
    NO_THREAT = "NO_THREAT"

# Read training data from CSV file
data = pd.read_csv('training_data.csv')
train_x = data['text'].tolist()
train_y = data['label'].tolist()

# Function to get average token vectors for a document
def get_doc_vector(doc):
    token_vectors = np.array([token.vector for token in doc if token.has_vector])
    if token_vectors.size == 0:
        return np.zeros((768,))
    return np.mean(token_vectors, axis=0)

# Generate vectors for training data
docs = [nlp(text) for text in train_x]
train_x_vectors = np.array([get_doc_vector(doc) for doc in docs])

# Debugging: Print out the shapes and sample vectors
print("Training vectors shape:", train_x_vectors.shape)
print("Sample training vector:", train_x_vectors[0])

# Ensure the vectors have the correct shape
if train_x_vectors.shape[1] == 0:
    print("Error: Training vectors are empty!")
else:
    # Initialize and train the SVM model
    clf_svm = svm.SVC(kernel='linear')
    clf_svm.fit(train_x_vectors, train_y)

    # Save the model
    joblib.dump(clf_svm, 'svm_model.pkl')
    print("Model saved to svm_model.pkl")

    # Example test data
    test_x = ["I found a suspicious package outside."]
    docs = [nlp(text) for text in test_x]
    test_x_vectors = np.array([get_doc_vector(doc) for doc in docs])

    # Debugging: Print out the shapes and sample vectors
    print("Test vectors shape:", test_x_vectors.shape)
    print("Sample test vector:", test_x_vectors[0])

    # Predict using the SVM model
    predictions = clf_svm.predict(test_x_vectors)
    print("Predictions:", predictions)
