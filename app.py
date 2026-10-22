import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(
page_title="ScamShield AI",
page_icon="🛡️"
)

st.title("🛡️ ScamShield AI")
st.subheader("AI-Powered Fraud Detection System")

st.write("Check a message using our machine-learning demo.")

st.warning(
"This is a demo model. Predictions may be incorrect. "
"Never share passwords or OTPs."
)

MODEL_PATH = Path(__file__).parent / "scam_message_model.joblib"

if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)

    message = st.text_area("Enter your message")

    if st.button("Analyze Message"):
        if message.strip():
            prediction = model.predict([message])[0]

            if prediction == "scam":
                st.error("⚠️ Potential Scam Detected")
            else:
                st.success("Classified as Legitimate")
        else:
            st.warning("Please enter a message.")
else:
    st.error("Model not found. Run python train_model.py first.")