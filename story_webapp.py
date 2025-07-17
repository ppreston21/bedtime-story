import streamlit as st
from openai import OpenAI
import os

# Unified API key loader: secrets (for Cloud), .env (for local)
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found. Please set it in .env or Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("🦄 Bedtime Story Generator")

topic = st.text_input("Enter a topic for your bedtime story:")

if st.button("Generate Story") and topic:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Write a one-sentence bedtime story about {topic}."}]
    )
    st.success(response.choices[0].message.content)
