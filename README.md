# 🛡️ Financial Phishing Email Detector

An NLP-based machine learning system that detects whether an email is **Phishing** or **Legitimate** using **TF-IDF feature extraction and Support Vector Machine (SVM)**.

The final Version 2 model was trained and evaluated on a combined dataset containing **115,164 emails** collected from multiple email datasets.

---

## 📌 Project Overview

Phishing emails are designed to trick users into revealing sensitive information such as passwords, banking credentials, OTPs, financial information, or personal data.

This project uses Natural Language Processing and Machine Learning to automatically classify email content as:

* ✅ Legitimate
* 🚨 Phishing

The system provides a simple Streamlit interface where users can paste an email and receive an instant prediction.

---

## 🎯 Objectives

* Detect phishing emails automatically using NLP.
* Combine multiple email datasets to improve model robustness.
* Clean and preprocess email data.
* Convert textual email content into numerical features using TF-IDF.
* Compare multiple machine learning algorithms.
* Select the best-performing model using multiple evaluation metrics.
* Build a reusable prediction pipeline.
* Deploy the final model through a Streamlit application.

---

## 📊 Dataset

Version 2 combines three email datasets:

1. Phishing Email Dataset
2. Enron Email Dataset
3. Nigerian Fraud Email Dataset

### Dataset Processing

The combined dataset initially contained duplicate and empty records.

After preprocessing:

* Duplicate emails removed: **420**
* Empty email removed: **1**
* Final dataset size: **115,164 emails**

The final dataset was divided into training and testing sets for model development and evaluation.

> The raw email datasets are not included in this repository because of dataset size, redistribution considerations, and potential privacy concerns.

---

## 🔄 Machine Learning Pipeline

```text
Raw Email
    ↓
Data Cleaning
    ↓
Duplicate Removal
    ↓
Text Preprocessing
    ↓
Train/Test Split
    ↓
TF-IDF Vectorization
    ↓
Machine Learning Models
    ↓
Model Evaluation
    ↓
Best Model Selection
    ↓
SVM Model
    ↓
Prediction Pipeline
    ↓
Streamlit Application
```

---

## 🧠 NLP Technique

### TF-IDF

Term Frequency-Inverse Document Frequency (TF-IDF) converts email text into numerical feature vectors.

It gives greater importance to words that are informative for distinguishing between phishing and legitimate emails while reducing the importance of very common words.

---

## 🤖 Models Compared

Two machine learning algorithms were evaluated:

### 1. Naive Bayes

Evaluation results:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 97.78% |
| Precision | 99.03% |
| Recall    | 96.70% |
| F1-score  | 97.85% |

### 2. Support Vector Machine

Evaluation results:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **99.51%** |
| Precision | **99.41%** |
| Recall    | **99.64%** |
| F1-score  | **99.53%** |
| ROC-AUC   | **99.98%** |

---

## 🏆 Final Model

### Support Vector Machine (SVM)

SVM was selected as the final Version 2 model because it outperformed Naive Bayes across the major evaluation metrics.

The model achieved:

**99.51% Accuracy**

**99.41% Precision**

**99.64% Recall**

**99.53% F1-score**

**99.98% ROC-AUC**

---

## 📈 Confusion Matrix

The SVM confusion matrix was:

```text
                 Predicted
                 Legitimate  Phishing

Actual Legitimate    10933       71
Actual Phishing         43    11986
```

### Interpretation

* True Negatives: **10,933**
* False Positives: **71**
* False Negatives: **43**
* True Positives: **11,986**

The model correctly identified the large majority of both legitimate and phishing emails.

---

## 🖥️ Streamlit Application

The application provides a simple interface where users can:

1. Enter or paste an email.
2. Click **Detect Phishing**.
3. Receive a prediction.
4. View whether the email is classified as:

   * 🚨 Phishing
   * ✅ Legitimate

---

## 📁 Project Structure

```text
Financial-Phishing-Email-Detector/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│
├── models/
│   ├── svm_model_v2.pkl
│   └── tfidf_vectorizer_v2.pkl
│
├── notebooks/
│
└── src/
    └── predict.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd Financial-Phishing-Email-Detector
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

From the project root directory:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🧪 Example

### Example Phishing Email

```text
URGENT! Your bank account will be suspended.
Click the link immediately to verify your account
and provide your password and OTP.
```

### Expected Result

```text
🚨 PHISHING EMAIL DETECTED
```

### Example Legitimate Email

```text
Hi John,

Please find attached the meeting agenda for tomorrow.
Let me know if you have any questions.

Regards,
David
```

### Expected Result

```text
✅ LEGITIMATE EMAIL
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF
* Support Vector Machine
* Naive Bayes
* Joblib
* Streamlit
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git & GitHub

---

## 🔍 Key Features

* NLP-based email classification
* Multi-dataset training
* Duplicate removal
* TF-IDF text representation
* Machine learning model comparison
* SVM-based final classifier
* High phishing detection recall
* Confusion matrix evaluation
* Reusable prediction pipeline
* Streamlit web interface

---

## 🚀 Future Improvements

Although Version 2 is the final scope of this project, possible future research directions include:

* Transformer-based models such as BERT
* Email header analysis
* URL and domain analysis
* Explainable AI
* Real-time email integration
* REST API deployment
* Model monitoring and retraining

---

## 👩‍💻 Author

**Greeshma Reddy**

B.Tech Graduate | Data Science & Machine Learning Enthusiast

---

## ⭐ Conclusion

The Financial Phishing Email Detector demonstrates how Natural Language Processing and Machine Learning can be applied to a real-world cybersecurity problem.

The final Version 2 system combines multiple email datasets, applies TF-IDF feature extraction, compares machine learning algorithms, and uses an SVM classifier achieving **99.51% accuracy and 99.53% F1-score** on the evaluation dataset.

The trained model is integrated into a Streamlit application to provide an interactive phishing email detection system.
