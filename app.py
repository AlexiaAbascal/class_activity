import streamlit as st

st.set_page_config(page_title="Heart Failure Classifier", layout="centered")

st.title("❤️ Welcome to the Heart Classification App")

st.markdown("""
Use the sidebar to navigate between pages:

- **Classifier**: Input your heart measurements to get a heart attack prediction.
- **About**: Learn more about the dataset and model.
""")