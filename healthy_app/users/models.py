from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.ppg', upload_to='profile_pics')


    def __str__(self):
        return f'Profile of {self.user.get_full_name()}'


