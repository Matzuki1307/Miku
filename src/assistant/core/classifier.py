
from assistant.integrations.ollama import send_chat_message

_SYSTEM_PROMPT = """
Eres un clasificador.

Debes responder EXCLUSIVAMENTE con una de estas opciones:

FIREFOX
STEAM
HORA
CHAT

Si la intención es abrir un navegador usa FIREFOX.

Si la intención es jugar usa STEAM.

Si preguntan la hora usa HORA.

Todo lo demás usa CHAT.

No agregues explicaciones.
No agregues puntuación.
No inventes categorías.
"""


def clasificar(comando: str) -> str:
    """Devuelve la etiqueta clasificada por el modelo.

    Se mantiene la salida strip() para compatibilidad con el código
    existente.
    """
    respuesta = send_chat_message(
        model="llama3.2:3b",
        messages=[{"role": "system", "content": _SYSTEM_PROMPT}, {"role": "user", "content": comando}],
    )

    return respuesta.message.content.strip()
