import json

from django import forms

from .open_weather_map import get_city_info



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
        info = get_city_info(city_name)
        # достать данные из info
        lat = 0
        lon = 0
        return (city_name, (lat, lon))