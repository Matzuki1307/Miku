
def send_chat_message(model: str, messages: list):
    """Envoltorio mínimo alrededor de ollama.chat.

    El import se realiza en tiempo de ejecución para evitar fallos durante
    importación del paquete en entornos donde la dependencia no está
    instalada. Lanzamos un error claro si ollama no está disponible.
    """
    try:
        from ollama import chat
    except Exception as exc:  # pragma: no cover - entorno de desarrollo
        raise RuntimeError("La librería 'ollama' no está disponible") from exc

    return chat(model=model, messages=messages)
