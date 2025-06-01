import requests
from pprint import pprint

from django.conf import settings



api_key = settings.OPEN_WEATHER_MAP_API_KEY


def get_temp(city_name: str, forecast: bool=False) -> list|None:
    """получить погоду в городе на данный момент (при forecast==False по умолчанию),
    если forecast==True получить прогноз погоды в городе"""

    if forecast:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric&lang=ru"
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=ru"
    
    try:
        response = requests.get(url, timeout=5)
        result = response.json()
        # возвращаем результат, если по названию города были получены данные, иначе возвращаем None
        if str(result["cod"]) == "200":
            if not forecast:
                print(result)
            return result
    except requests.exceptions.RequestException as error:
        print(f"Ошибка {error} при обращении к url: {url}")
