# 🛡️ Financial Phishing Email Detector

A Machine Learning and NLP-based application that detects whether an email is **legitimate** or **phishing**.

The project uses **TF-IDF for text representation** and **Linear Support Vector Machine (SVM)** for classification. A Streamlit web application provides a simple interface where users can enter an email and receive an instant prediction.

---

## 📌 Project Overview

Phishing emails are fraudulent messages designed to trick users into revealing sensitive information such as passwords, banking details, account credentials, or other personal information.

This project aims to automatically classify emails into two categories:

- **0 → Legitimate Email**
- **1 → Phishing Email**

The system learns patterns from a labeled email dataset and uses those patterns to classify new, unseen email messages.

---

## 🎯 Objectives

- Detect phishing emails automatically using Machine Learning.
- Apply Natural Language Processing (NLP) techniques to email text.
- Convert email text into numerical features using TF-IDF.
- Train and compare Machine Learning classification models.
- Select the best-performing model.
- Build an interactive Streamlit web application.
- Provide a simple real-time phishing email detection system.

---

## 🗂️ Project Structure

```text
Financial-Phishing-Email-Detector/
│
├── data/
│   └── cleaned_phishing_email.csv
│
├── models/
│   ├── svm_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── 01_Data_Analysis.ipynb
│
├── src/
│   └── predict.py
│
├── siri/
│   └── Python virtual environment
│
├── app.py
├── requirements.txt
└── README.md
