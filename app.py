import streamlit as st
import ollama

st.set_page_config(page_title="AI Email Generator", page_icon="📧")

st.title("📧 AI Email Generator (Local LLM)")

purpose = st.text_input("Email Purpose")
recipient = st.text_input("Recipient")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Formal"])

if st.button("Generate Email"):
    prompt = f"""
    Write a {tone} email.

    Purpose: {purpose}
    Recipient: {recipient}

    Include:
    - Subject
    - Greeting
    - Email Body
    - Closing
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.subheader("Generated Email")
    st.write(response["message"]["content"])