from django.urls import path

from .views import CityList


urlpatterns = [
    path("", CityList.as_view(), name="city_list"),
]
