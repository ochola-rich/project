from django.db import models

# Create your models here.
class WeatherData(models.Model):
    location = models.CharField(max_length=255)
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()

class DiseaseOutbreak(models.Model):
    crop = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    reported_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

class Recommendation(models.Model):
    media_upload = models.ForeignKey('media_uploads.MediaUpload', on_delete=models.CASCADE, related_name='recommendations')
    recommendation_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
