""" Exersice 1 """
coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
match = {}
for index, value in enumerate(coin):
    match[value] = code[index]
print(match)


""" Exersice 2 """
import json
from time import strftime, gmtime

with open('acdc.json', 'r') as f:
    file = json.load(f)
    track_duration = sum(int(i["duration"]) for i in file['album']['tracks']['track'])
    print('Album length is: ', strftime('%H:%M:%S', gmtime(track_duration)))


""" Exersice 3 """
dictionary = ['a', 'b', 'c', 'd', 'e']
dict_elements = {k: i for k, i in enumerate(dictionary)}
print(dict_elements)


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
