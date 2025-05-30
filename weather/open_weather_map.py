import requests

from django.conf import settings



api_key = settings.OPEN_WEATHER_MAP_API_KEY
"""
def get_city_info(city_name: str) -> list|None:
    "Получить информацию по названию города"
    limit = 1
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}"
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка {error} при обращении к url: {url}")
        

def get_temperature(lat: float, lon: float):
    "получить температуру по координатам"
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка {error} при обращении к url: {url}")
"""

def get_temp(city_name: str) -> list|None:
    "получить данные о погоде по названию города"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Ошибка {error} при обращении к url: {url}")