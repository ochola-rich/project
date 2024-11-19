from django.db import models

# Create your models here.
class Farm(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    size_in_hectares = models.FloatField()

class Crop(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='crops')
    name = models.CharField(max_length=100)
    planting_date = models.DateField()
    expected_harvest_date = models.DateField()
    
class Livestock(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='livestock')
    type = models.CharField(max_length=100)  # e.g., cattle, poultry
    count = models.IntegerField()
    health_status = models.CharField(max_length=255)
