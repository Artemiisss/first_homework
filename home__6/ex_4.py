""" Exersice 4"""
from time import sleep
from datetime import datetime


def timer(function):
    for i in range(3, 0, -1):
        print(i)
        sleep(1)
    return function


@timer
def online_time():
    date_time = datetime.now().strftime('%H:%M')
    print(date_time)


if __name__ == '__main__':
    online_time()
