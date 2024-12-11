# import streamlit as st
# import google.generativeai as genai

# GEMINI_KEY = "AIzaSyCBkH0M07STjMtGNb6joyeZTMLTipVrMXk"

# genai.configre(api_key=GEMINI_KEY)
# model = genai.GenerativeModel("gemini-1.5-pro-latest")

# chat = model.start_chat(history=[])

# prompt = st.text_input('Prompt', value='Esperando a pergunta...')

# while prompt != "fim":
#     response = chat.send_message(prompt)
#     st.write(response)
#     prompt = st.text_input('Prompt', value='Esperando a pergunta...')

# st.title('Hello World')

import streamlit as st
import google.generativeai as genai

# Configuração da API GEMINI
GEMINI_KEY = "AIzaSyCBkH0M07STjMtGNb6joyeZTMLTipVrMXk"
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Função para interagir com a API GEMINI
def get_response_from_gemini(prompt, context=""):
    # Combine o contexto com o prompt do usuário
    full_prompt = (
        "Você é um assistente especializado em normas de segurança para ambientes industriais. "
        "Utilize as informações abaixo como referência ao responder:\n\n"
        f"{context}\n\n"
        "Agora, responda à pergunta do usuário de forma clara e sucinta.\n\n"
        f"Pergunta: {prompt}"
    )

    # Enviar mensagem ao modelo
    chat = model.start_chat(history=[])  # Inicia uma nova sessão de chat
    response = chat.send_message(full_prompt)  # Passa o prompt completo

    # Acessar diretamente o conteúdo do primeiro candidato
    return response.candidates[0].content  # Corrigido acesso ao atributo

# Interface Streamlit
st.set_page_config(page_title="Chatbot de Normas de Segurança", layout="wide")
st.title("Chatbot de Normas de Segurança em Ambientes Industriais")

# Exibir introdução
st.markdown("### Bem-vindo!")
st.markdown(
    """
    Este chatbot é projetado para ajudar você a encontrar informações sobre normas de segurança em ambientes industriais.
    Faça sua pergunta e deixe o sistema fornecer respostas claras e contextualizadas com base no documento **Workshop Rules and Safety Considerations**.
    """
)

# Entrada do usuário
prompt = st.text_input("Digite sua pergunta:", value="")

if st.button("Enviar"):
    if prompt:
        try:
            # Interagir com o modelo da API
            response = get_response_from_gemini(prompt)

            # Exibir a resposta
            st.markdown("### Resposta:")
            st.write(response)

        except Exception as e:
            st.error(f"Erro ao processar a solicitação: {e}")

# Finalizar
st.markdown("---")
st.markdown("**Powered by GEMINI**")
