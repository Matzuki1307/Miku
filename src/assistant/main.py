from assistant.core.classifier import clasificar
from assistant.core.dispatcher import dispatch


def main() -> None:
    while True:
        comando = input("Jarvis > ")

        if comando.lower() == "salir":
            break

        accion = clasificar(comando)

        dispatch(accion, comando)

        print("Clasificado como:", accion)
