
import json
import requests

api_key = '302045706e64933a664f4b4fcdbfb6bb'
lat = '54.7431'
lon = '55.9678'
part = 'hourly,daily'

request = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}')

print(request.content)




