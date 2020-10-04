from django.db import models
from geoposition.fields import GeopositionField
# Create your models here.
class Post(models.Model):
    address = models.CharField(max_length=50, null=True, blank=True)
    rating = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)




class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()