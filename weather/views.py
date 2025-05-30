import requests
import json

from django.shortcuts import render

from .forms import CityForm
from .open_weather_map import get_temperature



def index(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data["city_name"]
            # здесь получить температуру по координатам
            city_name, info = cd
            lat = info[0]["lat"]
            lon = info[0]["lon"]
            print(lat, lon, type(lat))
            temp_info = get_temperature(lat, lon)
            results = f"{city_name}-----{info}-----{temp_info}"
        else:
            city_name = None
            results = "ошибка при поиске города"
    else:
        form = CityForm()
        city_name = None
        results = None

    context = {"form": form, "city_name": city_name, "results": results}
    return render(request, "weather/index.html", context)