import requests

from django.conf import settings



api_key = settings.OPEN_WEATHER_MAP_API_KEY

def get_city_info(city_name: str) -> dict:
    limit = 1
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}"
    response = requests.get(url)
    return response.json()