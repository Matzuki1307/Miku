from assistant.integrations.ollama import send_chat_message


def handle_chat(comando: str) -> None:
    """Envía el comando al modelo como mensaje de usuario y muestra la
    respuesta.
    """
    respuesta = send_chat_message(
        model="llama3.2:3b",
        messages=[{"role": "user", "content": comando}],
    )
    print(respuesta.message.content)
