from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    profession = models.CharField(blank=True, max_length=80)

    def __str__(self):
        return self.email