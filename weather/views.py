import requests
import json
from pprint import pprint
from datetime import datetime

from django.shortcuts import render

from .forms import CityForm



def index(request):
    form = CityForm()
    city_name = None
    temp_now_info = None
    temp_forecast_info = None

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            # получаем данные о погоде, которые получили в форме
            city_name, temp_now, temp_forecast = form.cleaned_data["city_name"]

            # собираем только необходимые данные
            temp_now_info = {
                "dt": datetime.fromtimestamp(temp_now["dt"]),
                "temp": round(temp_now["main"]["temp"]),
                "icon": temp_now["weather"][0]["icon"]
            }

            # # собираем только необходимые данные
            temp_forecast_info = []
            for item in temp_forecast["list"]:
                item_dict = {
                    "dt": datetime.fromtimestamp(item["dt"]),
                    "temp": round(item["main"]["temp"]),
                    "icon": item["weather"][0]["icon"]
                }
                temp_forecast_info.append(item_dict)


    context = {
        "form": form,
        "city_name": city_name,
        "temp_now": temp_now_info,
        "temp_forecast": temp_forecast_info
    }
    return render(request, "weather/index.html", context)
