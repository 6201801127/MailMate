import streamlit as st
# import openai
from google import genai


client = genai.Client(api_key=st.secrets["OPENAI_API_KEY"])
# client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
    
You are an AI assitent. Write a reply to the following email using a {tone.lower()} tone:
email:
{email_text}

Reply:
"""
    # response = client.chat.completions.create(
    #     model = "gemini-2.5-flash",
    #     messages=[{"role": "user", "content": prompt}] 
    # )
    # return response.choices[0].message.content
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text