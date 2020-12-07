from django.db import models
from django.conf import settings
from datetime import date


class UserConsumption(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    food = models.CharField(max_length=200, default="")
    calories = models.IntegerField(default=None)
    fat = models.IntegerField(default=None)
    protein = models.IntegerField(default=None)
    carbohydrates = models.IntegerField(default=date.today())
    datestamp = models.DateField()

    def __str__(self):
        return f"{self.id}"


class CalorieGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    daily_calories = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.user} {self.daily_calories}"


class MacroGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    daily_fat = models.IntegerField(default=None)
    daily_protein = models.IntegerField(default=None)
    daily_carbohydrates = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.user} Fat: {self.daily_fat} Protein: {self.daily_protein} Carbs: {self.daily_carbohydrates}"







