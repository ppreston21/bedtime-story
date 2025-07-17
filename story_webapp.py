import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🦄 Bedtime Story Generator")

topic = st.text_input("Enter a topic for your bedtime story:")

if st.button("Generate Story") and topic:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Write a one-sentence bedtime story about {topic}."}]
    )
    st.success(response.choices[0].message.content)
