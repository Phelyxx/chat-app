from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username