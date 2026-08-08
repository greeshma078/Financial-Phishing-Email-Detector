import joblib

# Load saved model and TF-IDF vectorizer
model = joblib.load("../models/svm_model.pkl")
tfidf = joblib.load("../models/tfidf_vectorizer.pkl")


def predict_email(email_text):
    # Convert email text into TF-IDF features
    email_tfidf = tfidf.transform([email_text])

    # Make prediction
    prediction = model.predict(email_tfidf)[0]

    if prediction == 1:
        return "Phishing Email"
    else:
        return "Legitimate Email"