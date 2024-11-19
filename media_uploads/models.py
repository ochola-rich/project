from django.db import models

# Create your models here.
class MediaUpload(models.Model):
    farm = models.ForeignKey('farm_management.Farm', on_delete=models.CASCADE, related_name='media_uploads')
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    media_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    analysis_results = models.JSONField(null=True, blank=True)  # Stores AI analysis results
