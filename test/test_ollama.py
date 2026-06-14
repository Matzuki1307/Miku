from ollama import chat

respuesta = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Di hola en una sola frase."
        }
    ]
)

print(respuesta.message.content)
