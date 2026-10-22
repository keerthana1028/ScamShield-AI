import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Demonstration dataset

data = {
"message": [
"Claim your free prize now",
"You won a lottery send your details",
"Verify your bank account immediately",
"Click this link to claim your reward",
"Send your OTP to receive your prize",
"Your account is blocked verify now",
"Congratulations you won a cash reward",
"Pay a fee to receive your gift",
"Your class starts tomorrow morning",
"Please attend the project meeting",
"Your assignment deadline is Friday",
"The college bus arrives at eight",
"Please send the lecture notes",
"Your exam timetable is available",
"Let us meet at the college library",
"The project presentation is next week"
],
"label": [
"scam", "scam", "scam", "scam",
"scam", "scam", "scam", "scam",
"legitimate", "legitimate", "legitimate",
"legitimate", "legitimate", "legitimate",
"legitimate", "legitimate"
]
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
df["message"],
df["label"],
test_size=0.25,
random_state=42,
stratify=df["label"]
)

model = Pipeline([
("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Model evaluation:")
print(classification_report(
y_test,
predictions,
zero_division=0
))

joblib.dump(model, "scam_message_model.joblib")

print("Model saved successfully!")
