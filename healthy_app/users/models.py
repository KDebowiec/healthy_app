from django.db import models
from django.contrib.auth.models import User


class HealthyAppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'Profile of {self.user.get_full_name()}'


