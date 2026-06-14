import subprocess
from datetime import datetime

while True:
    comando = input("Jarvis > ")

    comando = comando.lower()

    if comando == "salir":
        break

    if "firefox" in comando:
        subprocess.Popen(["firefox"])
        print("Abriendo Firefox...")
        continue

    if "hora" in comando:
        print(datetime.now().strftime("%H:%M:%S"))
        continue

    if "steam" in comando:
        subprocess.Popen([
            "flatpak",
            "run",
            "com.valvesoftware.Steam"
        ])
        print("Abriendo Steam...")
        continue

    print("No entiendo ese comando.")
