from django.db import models

class Parts(models.Model):
    part_name = models.CharField(max_length=100)
    part_cat = models.CharField(max_length=100)
    part_detail = models.TextField(null=True)
    part_photo = models.ImageField(upload_to="gallery", null=True, blank=True)
    
    def __str__(self):
        return self. part_name

# Create your models here.
