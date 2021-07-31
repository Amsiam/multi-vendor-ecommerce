from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser,BaseUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

