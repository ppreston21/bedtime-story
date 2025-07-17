import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # 👈 This loads .env file from your root folder

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🦄 Bedtime Story Generator")

topic = st.text_input("Enter a topic for your bedtime story:")

if st.button("Generate Story") and topic:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Write a one-sentence bedtime story about {topic}."}]
    )
    st.success(response.choices[0].message.content)
