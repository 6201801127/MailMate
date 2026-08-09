# import streamlit as st
# import openai
# # from google import genai
# import google.generativeai as genai


# client = genai.Client(api_key=st.secrets["OPENAI_API_KEY"])
# # client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# # for model in client.models.list():
# #     print("model name ---------------", model.name)

# def generate_email_response(email_text, tone):
#     prompt = f"""
    
# You are an AI assitent. Write a reply to the following email using a {tone.lower()} tone:
# email:
# {email_text}

# Reply:
# """
#     # response = client.chat.completions.create(
#     #     model = "gemini-2.5-flash",
#     #     messages=[{"role": "user", "content": prompt}] 
#     # )
#     # return response.choices[0].message.content
#     response = client.models.generate_content(
#         model="gemini-flash-lite-latest",
#         contents=prompt,
#     )
#     return response.text
    
import google.generativeai as genai
import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-flash-latest")

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone.

Email:
{email_text}

Reply:
"""

    response = model.generate_content(prompt)
    return response.text