from django.db import models

# Create your models here.
class CommunityReport(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    crop_or_livestock = models.CharField(max_length=100)
    description = models.TextField()
