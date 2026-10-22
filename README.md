# 🛡️ ScamShield AI

### AI-Powered Fraud Detection System

ScamShield AI is a machine-learning-based web application that analyzes text messages and classifies them as potential scams or legitimate messages.

The project demonstrates how Natural Language Processing (NLP) and machine learning can be used to identify suspicious messages.

## 🚀 Features

* Analyze text messages.
* Classify messages as potential scams or legitimate.
* Simple and interactive web interface.
* Machine learning using TF-IDF and Logistic Regression.
* Real-time predictions through a Streamlit application.

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* Joblib

## 📂 Project Structure

```text
ScamShield-AI/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── scam_message_model.joblib
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd ScamShield-AI
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Train the model

```bash
python train_model.py
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

1. The user enters a text message.
2. TF-IDF converts the text into numerical features.
3. A Logistic Regression classifier predicts the message category.
4. The application displays the predicted category.

## ⚠️ Limitations

This project currently uses a small demonstration dataset. Its predictions are not sufficiently validated for real-world fraud detection.

A message classified as legitimate may still be fraudulent. Users should independently verify suspicious messages and never share passwords, OTPs, or banking details.

## 🔮 Future Improvements

* Train with a larger, reliable, labeled dataset.
* Improve model evaluation using precision, recall, and F1-score.
* Add suspicious URL analysis.
* Improve the user interface.
* Deploy the application online.
* Add explainable predictions.

## 👩‍💻 Project Status

Initial prototype — under development.

## 📄 Disclaimer

ScamShield AI is an educational project and should not be used as the sole basis for financial or security decisions.
