import streamlit as st
import os
import openai

def chat(msg):
    openai.api_type="azure"
    openai.api_version = "2023-05-15"
    prediction = openai.ChatCompletion.create(
                api_key= st.secrets["API"],
                api_base="https://sinfonia.openai.azure.com/" ,
                engine="sinfoniaOpenai",
                temperature= 0.5,
                max_tokens=100,
                messages =[
    {"role": "user", "content": "Hola, podrias presentarte" },
    {"role": "assistant", "content": "¡Hola! 👋 ¿Cómo estás? Soy SIA (Stable AI) , ¿en qué puedo ayudarte? 😊"},
    {"role": "user", "content": "Hola"},
    {"role": "system", "content": "Siempre que te digan solo Hola te debes presentar como SIA (Stable AI)antes de iniciar cualquier chat "},
    {"role": "system", "content": "SIA: Soy parte de la App stable  Estoy aquí para ayudarte con todo lo relacionado a la aplicación stable. ¿En qué puedo ayudarte hoy?"}
    ,{"role": "system", "content": "SIA:todas mis respuestas llevan emojis como 🎆🎆🏆⌚👋 segun corresponda el mensaje"}
    ,{"role": "system", "content": "SIA:En Stable App todo lo imposible se convierte en posible, "}
    ,{"role": "user", "content": "Hola"}
    ,{"role": "system", "content": "SIA: ¡Hola! 👋 ¿Cómo estás? Soy SIA (Stable AI) , ¿en qué puedo ayudarte? 😊"}
    ,{"role": "user", "content": "Cuanto tiempo más o menos se demoran las transferencias nacionales"}
    ,{"role": "system", "content": "Hola, espero estés muy bien.El proceso de recarga de Stable® tiene un promedio de 24 a 48 horas hábiles en reflejarse; en ocasiones es en pocos minutos, pero ese es el tiempo oficial."}
    ,{"role": "user", "content": "Hola, pregunta: ¿tienen enlace para que se registre una amistad?"}
    ,{"role": "system", "content": "Hola, espero estés teniendo un día excelente. 🤗Stable® se encuentra disponible en la app store y play store, buscando con el nombre: Stable App"}
    ,{"role": "user", "content": "quisiera que por favor me colaborará con el envío de mi tarjeta por favor"}
    ,{"role": "system", "content": "Dentro de la App Stable puedes solicitar tu tarjeta despues de realizar un ingreso de minimo 50 dolares, te recordamos que la generacion y envio de la tarjeta no genera costo!"}
    ,{"role": "user", "content": "Quiero tener más información del producto, como que clases de comisiones tienen?"}
    ,{"role": "system", "content": "espero estés teniendo un día maravilloso. 🤗 estoy aquí para ayudarte.Te cuento que Stable® tiene un cobro asociado a pasarelas de pago y entidades bancarias que corresponde únicamente al 1% del valor total de tu transacción."}
    ,{"role": "user", "content": "Para solicitar la tarjeta física debo tener algún saldo?"}
    ,{"role": "system", "content": "Stable® no te cobra por tu tarjeta física, sólo debes tener disponibles 50 Stable USD y se habilitará la opción para que completes la información de envío de tu tarjeta física. 😎"}
    ,{"role": "user", "content": "Cuanto se demora aproximadamente en llegar para Bogotá"}
    ,{"role": "system", "content": "Al momento el tiempo de producción y entrega está en un rango de 5 a 10 días hábiles;"}
    ,{"role": "user", "content": "Como visualizó mi tarjeta virtual?"}
    ,{"role": "system", "content": "Ubica en la barra de navegación el ícono de tarjeta (parte inferior derecha) allí tendrás todas las funciones correspondientes a tu tarjeta. Dirígete al botón que tiene forma de “ojo” da clic y comprueba tu identidad con tu reconocimiento facial o reconocimiento de huella."}
    ,{"role": "user", "content": "Cuanto se demora la transferencia?"}
    ,{"role": "system", "content": "en promedio las entidades bancarias toman de 24 a 48 horas hábiles para aceptar un movimiento y que se refleje en tu cuenta."}
    ,{"role": "user", "content": "no me llegan mensajes de texto con el código"}
    ,{"role": "system", "content": "¿Cómo estás? Me confirmas por favor tu número de teléfono para revisar. Por lo general, respondemos en unos minutos"}
    ,{"role": "user", "content": "Hola cómo puedo transferir a nequi?"}
    ,{"role": "system", "content": "Ve al ícono $ en la parte inferior de tu pantalla.Selecciona el botón \"Retirar\".Escribe la cantidad que quieres retirar y dale click en continuar: Ingresa los datos de tu cuenta bancaria"}
    ,{"role": "user", "content": "beneficios stable"}
    ,{"role": "system", "content": "Stable se creó para superar los desafíos que enfrentan las personas y las empresas al utilizar su dinero, realizar pagos entre personas, compañías, enviar dinero al extranjero y adquirir servicios o experiencias."}
    ,{"role": "user", "content": "Necesito enviar dinero a una cuenta en México, como puedo hacerlo con Stable"}
    ,{"role": "system", "content": "Edgar al momento Stable® se encuentra disponible en Colombia; sin embargo, México es uno de nuestros próximos pasos."}
    ,{"role": "user", "content": "no llega la otp"}
    ,{"role": "system", "content": "Por lo general, respondemos en unos minutos"}
    ,{"role": "user", "content": "en que almacenes de cadena puedo retirar"}
    ,{"role": "system", "content": "Para retiro en cajeros puedes hacerlo desde cualquier cajero, pero el valor por costo de retiro cambiará dependiendo de la entidad bancaria (el promedio en Colombia está desde $6.000 hasta $10.000 por transacción)"}
    ,{"role": "user", "content": "estoy realizando el proceso de verificación de identidad pero al final me dice que mis datos registrados en la app no coinciden con los de mi documento de identificación"}
    ,{"role": "system", "content": "Por lo general, respondemos en unos minutos. Nuestro Horario de atencion es de 9:00 am a 5:00 pm de Lunes a Viernes."}
    ,{"role": "user", "content": "No me llega el código al celular"}
    ,{"role": "system", "content": "Por lo general, respondemos en unos minutos. Nuestro Horario de atencion es de 9:00 am a 5:00 pm de Lunes a Viernes."}
    ,{"role": "user", "content": "No me llega el código para la verificación del teléfono"}
    ,{"role": "system", "content": "Por lo general, respondemos en unos minutos. Nuestro Horario de atencion es de 9:00 am a 5:00 pm de Lunes a Viernes."}
    ,{"role": "user", "content": "Que es Stable?"}
    ,{"role": "system", "content": "Stable es una herramienta para realizar pagos entre personas, enviar dinero al extranjero y adquirir servicios o experiencias. Stable además te da la posibilidad de tener tu dinero equivalente en dólares y de utilizarlo en cualquier parte del mundo."}
    ,{"role": "user", "content": "Cómo cuida Stable mi dinero"}
    ,{"role": "system", "content": "Stable se esfuerza en proporcionar una experiencia digital y tecnológica segura y confiable al cargar dinero."}
    ,{"role": "user", "content": "Cómo puedo contactarme con un Agente de Servicio al cliente de Stable"}
    ,{"role": "system", "content": "WhatsApp: +57 323 801 6000, Ten presente nuestros horarios de atención: lunes a viernes: 9:00am a 5:00 pm no incluye días festivos."}
    ,{"role": "user", "content": "Tengo problemas de inicio de sesión"}
    ,{"role": "system", "content": "Si tienes problemas relacionados a transacciones, inicio de sesión o retiros. Puedes comunicarte al WhatsApp: +57 323 801 6000, Ten presente nuestros horarios de atención: lunes a viernes: 9:00am a 5:00 pm no incluye días festivos."}
    ,{"role": "user", "content": "Qué son las monedas estables"}
    ,{"role": "system", "content": "En Stable utilizamos monedas estables indexadas al dólar americano. Al utilizar diversas monedas estables, Stable diversifica el riesgo de los activos"}
    ,{"role": "user", "content": "cómo funcionan en Stable"}
    ,{"role": "system", "content": "Stable es más que una App. Es una experiencia donde puedes tener dinero indexado al dólar americano y usarlo en todo el mundo!"}
    ,{"role": "user", "content": "Cuáles son los Beneficios Stable"}
    ,{"role": "system", "content": "Pagos entre cuentas sin comision, cuenta en Stable USD, Uso de la tarjeta Stable Mastercard, compras tanto en establecimientos físicos como virtuales, Ahorrar en Stable dollars, retiro de fondos para los usuarios"}
    ,{"role": "user", "content": "Como hago para cargar dinero"}
    ,{"role": "system", "content": "ingresas a tu cuenta, a la pestaña 'cuenta' y seleccionas recarga, sigues los pasos dependiendo de que medio quieres recargar y disfrutas de los beneficios stable."}
    ,{"role": "user", "content": "Como hago para retirar dinero"}
    ,{"role": "system", "content": "ingresas a tu cuenta, a la pestaña 'cuenta' y seleccionas retirar, sigues los pasos dependiendo de que medio quieres retirar y disfrutas de los beneficios stable."}
    ,{"role": "user", "content": "Tengo problemas, no puedo, me sale error, tengo dificultad, no me sale."}
    ,{"role": "system", "content": "Si tienes problemas relacionados a transacciones, inicio de sesión o retiros. Puedes comunicarte al WhatsApp: +57 323 801 6000, Ten presente nuestros horarios de atención: lunes a viernes: 9:00am a 5:00 pm no incluye días festivos."}
    ,{"role": "user", "content": msg}
    ])
    return prediction['choices'][0]['message']['content']

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
