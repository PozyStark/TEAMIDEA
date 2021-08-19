
import json
import requests
import datetime
import time
import math

api_key = '302045706e64933a664f4b4fcdbfb6bb'
lat = '54.7431'
lon = '55.9678'
part = 'minutely,hourly,alerts'

request = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}')

weather_data = json.loads(request.text)
current_data = ''
daily_data = ''

for key in weather_data:
    if key == 'daily':
        daily_data = weather_data[key]
    if key == 'current':
        current_data = weather_data[key]


def print_data(daily_values, msg=''):
    for day in daily_values:
        date = time.ctime(day['dt'])
        pressure = day['pressure']
        temp = day['temp']
        morn = temp['morn']
        night = temp['night']

        c_morning = round(morn - 273.15, 2)
        c_night = round(night - 273.15, 2)
        print(f'{msg} Date: {date} Pressure: {pressure} Morn: {c_morning} C Night: {c_night} C')


def max_pressure(data, lim):  # Функция возвращает dict с датой содержащей максимальное давление за пребстоящие дни lim
    result_day = None
    pressure_temp = 0
    for i in range(len(data) - 1):
        if i == lim:
            break
        date = data[i]
        pressure = date['pressure']
        if pressure_temp < pressure:
            pressure_temp = pressure
            result_day = data[i]
    return result_day


def min_delta_temp(daily_values):
    result_day = None
    delta_temp = math.inf
    for day in daily_values:
        date = time.ctime(day['dt'])
        temp = day['temp']
        morn = temp['morn']
        night = temp['night']
        delta = round(abs(morn - night), 3)
        if delta_temp > delta:
            delta_temp = delta
            result_day = day

    return result_day


print_data(daily_data)
print()

delta = min_delta_temp(daily_data)
pressure = max_pressure(daily_data, 5)

print_data([delta], 'Минимальная разница температур: ')
print_data([pressure], 'Максимальное давление за предстоящие 5 дней: ')



