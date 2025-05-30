import requests
import json

from django.shortcuts import render

from .forms import CityForm
from .open_weather_map import api_key



def index(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data["city_name"]
            # здесь получить температуру по координатам
            print(city_name)
            results = "всё хорошо"
        else:
            city_name = None
            results = "ошибка при поиске города"
    else:
        form = CityForm()
        city_name = None
        results = None

    context = {"form": form, "city_name": city_name, "results": results}
    return render(request, "weather/index.html", context)