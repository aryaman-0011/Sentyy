import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/analyze"

st.title("Basic Sentiment Analyzer")

# Input Section
text = st.text_area("Enter text to analyze sentiment:", "")

if st.button("Analyze"):
    if text.strip():
        response = requests.post(API_URL, json={"text": text})
        if response.status_code == 200:
            result = response.json()
            st.success(f"Sentiment: {result['sentiment']}")
            st.write(f"Polarity Score: {result['sentiment']['polarity']}")
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    else:
        st.warning("Please enter some text.")

# Footer
st.sidebar.title("About")
st.sidebar.info("This is a demo app to analyze Sentiments on the scale of -1 to 1.")
