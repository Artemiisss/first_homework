import csv
import requests
from requests import Response
from datetime import datetime as dt


def creating_file(name_file: str, data: list):
    with open(name_file, 'w') as f:
        writer = csv.DictWriter(f, delimiter='\t', fieldnames=data[0])
        writer.writeheader()
        for items in data:
            writer.writerow(items)


def saving_file(city: str, forecast: int) -> str:
    result = f'{dt.now().strftime("%d-%m-%Y")} {city.capitalize()} {forecast} days-weather-forecast.txt'
    return result.replace(' ', '-')


def date_of_weather(response: Response) -> list:
    result = []
    for dates in response['list']:
        result.append(dt.fromtimestamp(dates['dt']).strftime('%d-%m-%Y'))
    return result


def temperature_list(response: Response, key: str) -> list:
    result = []
    for temp in response['list']:
        result.append(float(temp['temp'][key]))
    return result


def average_temperature(response: Response) -> list:
    result = []
    for item in response['list']:
        average = round((item['temp']['max'] + item['temp']['min']) / 2, 2)
        result.append(float(average))
    return result


def temperature_data(d: list, average: list, day: list, night: list) -> list:
    result = []
    for dates, avg, _day, _night in zip(d, average, day, night):
        result.append({'date': dates, 'avg': avg, 'day': _day, 'night': _night})
    return result


def url_weather(city: str, forecast: int) -> str:
    return f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={forecast}' \
           f'&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8'


def url_json(url: str) -> Response:
    return requests.get(url).json()


def main():
    city_type = str(input('Enter your city: '))
    forecast_days = int(input('Enter how many days for forecast you need: '))
    url_link = url_weather(city_type, forecast_days)
    file = saving_file(city_type, forecast_days)
    response = url_json(url_link)
    dates_list = date_of_weather(response)
    avg_temperature = average_temperature(response)
    day_temperature = temperature_list(response, 'day')
    night_temperature = temperature_list(response, 'night')
    temperature_cons = temperature_data(dates_list, avg_temperature, day_temperature, night_temperature)
    creating_file(file, temperature_cons)


if __name__ == '__main__':
    main()