from datetime import datetime
from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='użytkownik healthy_app')
    datetime = models.DateTimeField(default=datetime.now)
    meal_json = models.JSONField(verbose_name='meal_plan_json')
    general_health = models.CharField(max_length=100, null=True)
    general_min_kcal = models.IntegerField(max_length=100, null=True)
    general_max_kcal = models.IntegerField(max_length=100, null=True)
    photo = models.ImageField(max_length=2000, null=True)
    page_title = models.CharField(max_length=1000, default='dish')
