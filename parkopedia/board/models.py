from django.db import models

# Create your models here.
class Post(models.Model):
    address = models.CharField(max_length=50, null=True, blank=True)
    rating = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

class MyPos(models.Model):
    lat = models.FloatField(default=42.697450)
    lon = models.FloatField(default=23.324280)