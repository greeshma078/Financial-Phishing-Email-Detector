import joblib
import os


# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Load Version 2 SVM model
MODEL_PATH = os.path.join(
    BASE_DIR, "models", "svm_model_v2.pkl"
)

# Load Version 2 TF-IDF vectorizer
VECTORIZER_PATH = os.path.join(
    BASE_DIR, "models", "tfidf_vectorizer_v2.pkl"
)


model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)


def predict_email(email_text):

    # Convert email text into TF-IDF features
    email_vector = tfidf.transform([email_text])

    # Predict
    prediction = model.predict(email_vector)[0]

    if prediction == 1:
        return "Phishing"
    else:
        return "Legitimate"