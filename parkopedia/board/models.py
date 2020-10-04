from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class Location(models.Model):
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mapbox/outdoors-v11", "marker_color": "blue", "center": (17.031645, 51.106715)})
    create= models.DateTimeField(auto_now_add=True)
    address = AddressAutoHiddenField()
    
