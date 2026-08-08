import streamlit as st
import joblib

# Load trained model and TF-IDF vectorizer
model = joblib.load("models/svm_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

# Page configuration
st.set_page_config(
    page_title="Financial Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)

# Title
st.title("🛡️ Financial Phishing Email Detector")

st.write(
    "Analyze an email and determine whether it is "
    "legitimate or potentially a phishing email."
)

# Email input
email_text = st.text_area(
    "📧 Enter Email Text",
    height=250,
    placeholder="Paste the email content here..."
)

# Prediction button
if st.button("🔍 Check Email"):

    if email_text.strip() == "":
        st.warning("Please enter an email message.")

    else:
        # Convert email into TF-IDF features
        email_tfidf = tfidf.transform([email_text])

        # Make prediction
        prediction = model.predict(email_tfidf)[0]

        # Display result
        if prediction == 1:
            st.error("🚨 Phishing Email Detected!")

        else:
            st.success("✅ Legitimate Email")