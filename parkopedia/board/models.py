from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField

# Create your models here.
class Post(models.Model):
    address = models.CharField(max_length=50, null=True, blank=True)
    rating = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

class MyPos(models.Model):
    lat = models.FloatField(default=42.697450)
    lon = models.FloatField(default=23.324280)

class Location(models.Model):
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mapbox/outdoors-v11", "marker_color": "blue", "center": (17.031645, 51.106715)})
    create= models.DateTimeField(auto_now_add=True)
    address = AddressAutoHiddenField()
    
