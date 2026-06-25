from datetime import datetime


def get_time():
    while True:
        current_time = datetime.now()
        print(current_time.strftime("%H:%M:%S"), end="\r")

get_time()