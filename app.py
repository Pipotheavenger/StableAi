import streamlit as st
import os
from openai import OpenAI
import time

client = OpenAI(api_key=st.secrets["API"])
def chat(msg):
    ASSISTANT_ID="asst_YAL99pcWX17Qun3bsBMlUKdp"
    thread = client.beta.threads.create(
        messages=[
            {"role":"user","content":msg}
        ]
    )
    run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=ASSISTANT_ID)
    #print("run created : {run.id}")
    #wait for run to complete it
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
        #print("run status : {run.status}")
        time.sleep(1)
    else:
        #print("run completed")
        pass
    message_response = client.beta.threads.messages.list(thread.id)
    last = message_response.data[0]
    return str(last.content[0].text.value)

def main():
    st.set_page_config(page_title="Chatbot SIA", layout="wide")

    # Estilo para el fondo y la conversación, diferenciando mensajes de usuario y bot
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: white;
        }
        .stTextInput>div>div>input {
            border-radius: 20px;
            padding: 10px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 20px;
            background-color: #6a11cb;
            color: white;
        }
        /* Estilos para mensajes de usuario y bot */
        .user-message textarea {
            background-color: #007bff !important; /* Blue for user messages */
            color: white !important;
        }
        .bot-message textarea {
            background-color: #7fffd4 !important; /* Aquamarine for bot messages */
            color: black !important;
        }
        textarea {
            border: none !important;
            width: 100% !important;
            resize: none !important; /* Disable resizing */
        }
        .fixed-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 5px 10px;
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header del chatbot
    st.sidebar.image("https://play-lh.googleusercontent.com/N4jH4JgPV_UmiPllkg8xQRmPPXr20LmcHoLJrkr8uSkumD3QIbZuiYHMADZzk-btKSO1", width=100, output_format='auto', use_column_width=True)
    st.sidebar.title("SIA (Stable IA)")
    st.sidebar.header("🌟 ¡Hola! Bienvenido a Stable®")
    st.sidebar.write("¿Listo para ser residente de un mundo diseñado para enriquecer tu vida con oportunidades emocionantes? Descargar Stable es completamente gratis y es tu primer paso hacia una vida llena de aventuras. ❤️ ¡Dime cómo puedo ayudarte hoy!")

    # Gestión de conversaciones
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""

    # Mostrar la conversación con diferentes colores para el usuario y el bot
    for label, message in st.session_state.conversation:
        st.container().markdown(f"<div class='{label.lower().replace(' ', '-')}-message'><textarea disabled>{label}: {message}</textarea></div>", unsafe_allow_html=True)

    # Crear una barra fija al pie de la página para el input y el botón
    with st.container():
        st.markdown("<div class='fixed-footer'>", unsafe_allow_html=True)
        user_input = st.text_input("Escribe tu pregunta aquí...", value=st.session_state.input_text, key="input", placeholder="Type here...")
        send_button = st.button("Send")
        st.markdown("</div>", unsafe_allow_html=True)

    if send_button and user_input:
        st.session_state.conversation.append(("👤 Usuario", user_input))
        # Procesamiento de la pregunta para generar una respuesta
        response = chat(user_input)  # Asumiendo que tienes una función `chat` en tu módulo Azure
        st.session_state.conversation.append(("🧙‍♂️ SIA", response))
        st.session_state.input_text = ""  # Clear input box after sending the message
        st.rerun()

if __name__ == "__main__":
    main()
