from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo=models.ImageField(upload_to="user_photos/", default="media/photo_2024-01-17_01-35-37.jpg" )
    phone_number=models.CharField(max_length=13, unique=True, blank=True, null=True)