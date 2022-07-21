"""Написати калькулятор температури.
    Користувач вводить число та тип температури (C, F, K - Цельсій, Фарренгейт, Кельвін відповідно)
    Програма має вивести температуру у трьох шкалах температур – Цельсій, Фарренгейт, Кельвін."""


temperature = int(input('Enter temperature:'))
type_temp = input('Choose Celsius as C, Fahrenheit as F, Kelvin as K:')
if type_temp == 'C':
    print(f'\nTemperature in Celsius: {temperature}')
    print(f'Temperature in Fahrenheit: {((temperature * 1.8) + 32) // 1}')
    print(f'Temperature in Kelvin: {(temperature + 273.15) // 1}')
elif type_temp == 'F':
    print(f'\nTemperature in Fahrenheit: {temperature}')
    print(f'Temperature in Celsius: {((temperature -32) / 1.8) // 1 }')
    print(f'Temperature in Kelvin: {((temperature + 459.67) * 5 /9) // 1}')
elif type_temp == 'K':
    print(f'\nTemperature in Kelvin: {temperature}')
    print(f'Temperature in Fahrenheit: {((temperature - 273.15) * 9 /5 + 32) // 1}')
    print(f'Temperature in Celsius: {(temperature - 273.15 // 1)}')
else:
    print('Not invalid symbol')