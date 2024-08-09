from django.db import models
from django.contrib.auth.models import User


class Exercises(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='użytkownik healthy_app', null=True)
    descriptions = models.TextField()
    muscle = models.CharField(max_length=100, null=True)
    difficulty = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.muscle


