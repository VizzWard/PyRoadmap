from django.db import models

from test_s3.storage import PublicMediaStorage

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(storage=PublicMediaStorage(), upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)