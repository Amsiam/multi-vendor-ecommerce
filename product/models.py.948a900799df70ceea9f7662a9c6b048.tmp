from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)