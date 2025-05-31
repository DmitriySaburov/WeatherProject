from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Город"
    )
    search_count = models.BigIntegerField(
        default=0,
        verbose_name="Кол-во запросов"
    )

    def __str__(self):
        return f"{self.name}"
    
    def increase_search_count(self):
        """Увеличивает счетчик кол-ва запросов"""
        self.search_count += 1
        self.save()
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class CitySearch(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name="Город"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время запроса"
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "История поиска"
        verbose_name_plural = "Истории поиска"
    
    def __str__(self):
        return f"{self.user.username} -> {self.city.name} ({self.created})"
