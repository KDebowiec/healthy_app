from django.db import models


class Exercises(models.Model):
    descriptions = models.TextField()

    def __str__(self):
        return self.email
