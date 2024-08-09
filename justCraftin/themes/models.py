from django.db import models

#model for theme
class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()
