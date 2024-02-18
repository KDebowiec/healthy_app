from django.db import models


class Exercises(models.Model):
    email = models.EmailField(unique=False)
    descriptions = models.TextField()

    def __str__(self):
        return self.email
