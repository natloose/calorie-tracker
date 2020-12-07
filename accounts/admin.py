from django.contrib import admin
from .models import UserConsumption, CalorieGoal, MacroGoal
# Register your models here.

admin.site.register(UserConsumption)
admin.site.register(CalorieGoal)
admin.site.register(MacroGoal)
