import streamlit as st
import joblib
import pandas as pd

# Page config
st.set_page_config(
    page_title="AI Jailbreak Detector",
    page_icon="🛡️",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    clf = joblib.load('models/classifier.joblib')
    vectorizer = joblib.load('models/tfidf_vectorizer.joblib')
    return clf, vectorizer

clf, vectorizer = load_model()

# UI
st.title("🛡️ AI Jailbreak Detector")
st.markdown("Type a prompt below to check if it's a **jailbreak attempt** or a **normal question**.")

prompt = st.text_area("Enter a prompt:", height=150)

if st.button("Analyze"):
    if prompt.strip():
        X = vectorizer.transform([prompt])
        prob = clf.predict_proba(X)[0][1]
        label = "🔴 Jailbreak" if prob >= 0.5 else "🟢 Normal"

        st.markdown("---")
        col1, col2 = st.columns(2)
        col1.metric("Prediction", label)
        col2.metric("Jailbreak Confidence", f"{prob*100:.1f}%")
    else:
        st.warning("Please enter a prompt first.")