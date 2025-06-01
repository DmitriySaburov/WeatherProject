from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import CityForm
from .models import City, CitySearch



def index(request):
    form = CityForm()
    city_name = None
    temp_now_info = None
    temp_forecast_info = None
    search_history = None

    if request.method == "GET":
        if request.user.is_authenticated:
            # получаем историю поиска пользователя
            search_history = CitySearch.objects.filter(
                user=request.user
            )

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            # получаем данные о погоде, которые получили в форме
            city_name, temp_now, temp_forecast = form.cleaned_data["city_name"]

            # собираем только необходимые данные
            temp_now_info = {
                "dt": datetime.utcfromtimestamp(temp_now["dt"] + temp_now["timezone"]),
                "temp": round(temp_now["main"]["temp"]),
                "icon": temp_now["weather"][0]["icon"]
            }

            temp_forecast_info = []
            for item in temp_forecast["list"]:
                item_dict = {
                    "dt": datetime.fromtimestamp(item["dt"]),
                    "temp": round(item["main"]["temp"]),
                    "icon": item["weather"][0]["icon"]
                }
                temp_forecast_info.append(item_dict)
            
            # добавляем город в БД или обновляем счетчик запросов
            try:
                city = City.objects.get(name=city_name)
                city.increase_search_count()
            except City.DoesNotExist:
                city = City.objects.create(name=city_name)
            
            # если пользователь авторизован
            if request.user.is_authenticated:
                # получаем историю поиска пользователя
                search_history = CitySearch.objects.filter(
                    user=request.user
                )

                # обновляем историю поиска
                city_search = CitySearch.objects.create(
                    user=request.user,
                    city=city
                )

    context = {
        "form": form,
        "city_name": city_name,
        "temp_now": temp_now_info,
        "temp_forecast": temp_forecast_info,
        "search_history": search_history
    }
    return render(request, "weather/index.html", context)
