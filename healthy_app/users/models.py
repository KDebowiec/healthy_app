from django.db import models
from django.contrib.auth.models import User


class HealthyAppUser(models.Model):
    user = models.OneToOneField(User)
    meal_plans = models.KLUCZ_OBCY