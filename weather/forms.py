import json

from django import forms

from .open_weather_map import get_temp



class CityForm(forms.Form):
    city_name = forms.CharField(
        max_length=200,
        required=True,
        label="Город:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "Enter city name..."
            }
        )
    )

    def clean_city_name(self) -> tuple|None:
        city_name = self.cleaned_data["city_name"]

        # пробуем получить информацию о температуре
        temp_now = get_temp(city_name)
        temp_forecast = get_temp(city_name, forecast=True)
        
        # если удалось получить информацию о погоде, то передаем данные о погоде вместе с названием города
        if temp_now and temp_forecast:
            # берем название города из данных о температуре
            city_name = temp_now["name"]
            return (city_name, temp_now, temp_forecast)
        else:
            raise forms.ValidationError("Не удалось получить данные по названию города")