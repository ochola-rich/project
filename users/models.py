from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    FARMER = 'Farmer'
    AGRONOMIST = 'Agronomist'
    ADMIN = 'Admin'
    
    ROLE_CHOICES = [
        (FARMER, 'Farmer'),
        (AGRONOMIST, 'Agronomist'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=FARMER)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=255, blank=True)
