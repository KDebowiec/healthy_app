from django.db import models
from django.contrib.auth.models import User
from nutrition import models as nutrition_models


class HealthyAppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    meal_plans = models.ForeignKey(nutrition_models.MealPlan, on_delete=models.CASCADE)
