from datetime import datetime


def print_time() -> None:
    print(datetime.now().strftime("%H:%M:%S"))
