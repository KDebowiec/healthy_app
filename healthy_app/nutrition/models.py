from datetime import datetime
from django.db import models
from users.models import HealthyAppUser


class MealPlan(models.Model):
    healthy_app_user = models.ForeignKey(HealthyAppUser, on_delete=models.CASCADE, verbose_name='użytkownik healthy_app')
    datetime = models.DateTimeField(default=datetime.now)
    meal_json = models.JSONField(verbose_name='meal_plan_json')


