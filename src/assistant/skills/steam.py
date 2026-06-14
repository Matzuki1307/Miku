import subprocess


def open_steam() -> None:
    subprocess.Popen(["flatpak", "run", "com.valvesoftware.Steam"])
