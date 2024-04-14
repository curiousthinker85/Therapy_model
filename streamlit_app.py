# streamlit_app.py
import streamlit as st
import requests

LLM_API_URL = "http://localhost:8000"

st.title("LLM Web App")

prompt = st.text_input("Enter your prompt")

if st.button("Generate"):
    data = {"prompt": prompt}
    response = requests.post(LLM_API_URL, json=data)
    generated_text = response.json()["response"]
    st.write(generated_text)
