"""Shim de compatibilidad: expone la interfaz anterior pero
delegando la implementación en el paquete assistant.

Al ejecutar este archivo se lanza el REPL definido en
src/assistant/main.py.
"""

from assistant.main import main


if __name__ == "__main__":
    main()
