import streamlit as st
import sys
import os

# --------------------------------------------------
# Project Configuration
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

sys.path.append(SRC_DIR)

from predict import predict_email


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Financial Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)


# --------------------------------------------------
# Custom Styling
# --------------------------------------------------

st.markdown(
    """
    <style>
        .main {
            padding-top: 2rem;
        }

        .title {
            text-align: center;
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }

        .subtitle {
            text-align: center;
            color: #666666;
            font-size: 1rem;
            margin-bottom: 2rem;
        }

        .footer {
            text-align: center;
            color: #888888;
            font-size: 0.85rem;
            margin-top: 3rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="title">🛡️ Financial Phishing Email Detector</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze an email and identify whether it is legitimate or potentially phishing.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Email Input
# --------------------------------------------------

st.subheader("📧 Email Analysis")

email_text = st.text_area(
    "Enter email content",
    height=250,
    placeholder=(
        "Paste the email message here...\n\n"
        "Example:\n"
        "Your account requires immediate verification. "
        "Please click the link below to confirm your details."
    ),
    label_visibility="visible"
)


# --------------------------------------------------
# Buttons
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    detect_button = st.button(
        "🔍 Detect Phishing",
        use_container_width=True
    )

with col2:
    clear_button = st.button(
        "🗑️ Clear",
        use_container_width=True
    )


# --------------------------------------------------
# Clear Input
# --------------------------------------------------

if clear_button:
    st.rerun()


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if detect_button:

    if not email_text.strip():

        st.warning("Please enter an email message to analyze.")

    else:

        result = predict_email(email_text)

        st.markdown("---")

        st.subheader("🔎 Analysis Result")

        if result == "Phishing":

            st.error(
                "🚨 PHISHING EMAIL DETECTED"
            )

            st.write(
                "This email has been classified as potentially "
                "phishing by the detection model."
            )

            st.warning(
                "Avoid clicking links, downloading attachments, "
                "or sharing sensitive information until the email "
                "is verified."
            )

        else:

            st.success(
                "✅ LEGITIMATE EMAIL"
            )

            st.write(
                "This email has been classified as legitimate "
                "by the detection model."
            )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'Financial Phishing Email Detector • NLP & Machine Learning'
    '</div>',
    unsafe_allow_html=True
)