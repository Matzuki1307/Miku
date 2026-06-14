import subprocess


def open_firefox() -> None:
    subprocess.Popen(["firefox"])
    print("Abriendo Firefox...")
