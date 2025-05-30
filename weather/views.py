import requests
import json
from pprint import pprint

from django.shortcuts import render

from .forms import CityForm



def index(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data["city_name"]
            # здесь получить температуру по координатам
            city_name, info = cd
            print(type(info))
            pprint(info)
            results = info
        else:
            city_name = None
            results = "ошибка при поиске города"
    else:
        form = CityForm()
        city_name = None
        results = None

    context = {"form": form, "city_name": city_name, "results": results}
    return render(request, "weather/index.html", context)