import streamlit as st
import google.generativeai as genai

GEMINI_KEY = "AIzaSyCBkH0M07STjMtGNb6joyeZTMLTipVrMXk"

genai.configre(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

chat = model.start_chat(history=[])

prompt = st.text_input('Prompt', value='Esperando a pergunta...')

while prompt != "fim":
    response = chat.send_message(prompt)
    st.write(response)
    prompt = st.text_input('Prompt', value='Esperando a pergunta...')

st.title('Hello World')

