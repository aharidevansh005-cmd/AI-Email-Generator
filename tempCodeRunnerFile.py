import streamlit as st
import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="AQ.Ab8RN6KVfHh8Otd9sWqpL2pMUziBp1QRWhf0bEfOMD5kBfbuDg")

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page Settings
st.set_page_config(page_title="AI Email Generator", page_icon="📧")

# UI
st.title("📧 AI Email Generator")
st.write("Generate professional emails using Generative AI.")

purpose = st.text_input("Email Purpose")
recipient = st.text_input("Recipient")

tone = st.selectbox(
    "Tone",
    ["Professional", "Friendly", "Formal"]
)

if st.button("Generate Email"):

    prompt = f"""
    Write a {tone} email.

    Purpose:
    {purpose}

    Recipient:
    {recipient}

    Include:
    Subject
    Greeting
    Email Body
    Closing
    """

    response = model.generate_content(prompt)

    st.subheader("Generated Email")
    st.write(response.text)