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

    def clean_city_name(self):
        city_name = self.cleaned_data["city_name"]
        # пробуем получить информацию о городе у API openweathermap
        info = get_temp(city_name)
        # добавляем info к названию города
        if info:
            return (city_name, info)
        else:
            raise forms.ValidationError("Не удалось получить данные по названию города")