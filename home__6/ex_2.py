""" Exersice 2 """
import json
from time import strftime, gmtime

with open('acdc.json', 'r') as f:
    file = json.load(f)
    track_duration = sum(int(i["duration"]) for i in file['album']['tracks']['track'])
    print('Album length is: ', strftime('%H:%M:%S', gmtime(track_duration)))