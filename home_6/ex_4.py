""" Exersice 4"""
from datetime import datetime
from time import sleep


def countdown(function):
    def wrapper(*args, **kwargs):
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        function(*args, **kwargs)

    return wrapper


@countdown
def online_time():
    date_time = datetime.now().strftime('%H:%M')
    print(date_time)


if __name__ == '__main__':
    online_time()
