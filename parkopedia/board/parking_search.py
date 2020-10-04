import googlemaps
import pprint
import time
from math import asin, cos, radians, sin, sqrt

#from GoogleMapsAPIKey import get_my_key
#from Auto_search import ready()


lat1 = -33.8670522 
lng1 = 151.195362


def locations(lat1, lng1):
    #API_KEY = get_my_key()
    locations_dict = dict()
    API_KEY = 'AIzaSyCndiwpn0s7MRo2qbhPbzhSxdODyPkFDBo'
    gmaps = googlemaps.Client(key = API_KEY)
    places_result = gmaps.places_nearby(location = (lat1, lng1 ), radius = 200, open_now = False, type = 'parking')

    for place in places_result['results']:
        name = None
        lat = None
        lng = None

        my_place_id = place['place_id']
        my_fields = ['name','geometry']
        place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
        name = place_details['result']['name']
        lat = place_details['result']['geometry']['location']['lat']
        lng = place_details['result']['geometry']['location']['lng']
        locations_dict.update ({name: [lat, lng]})
    return locations_dict


def dist_between_two(*args):
    lat1, lat2, long1, long2 = map(radians, args)

    dist_lats = abs(lat2 - lat1) 
    dist_longs = abs(long2 - long1) 
    a = sin(dist_lats/2) + cos(lat1) * cos(lat2) * sin(dist_longs/2)
    c = asin(sqrt(a)) * 2
    radius_earth = 6378 
    return c * radius_earth


def nearest(lat1,lng1):
    places = locations(lat1,lng1)

    best = list()
    for lat2,lng2 in places.values():
        best.append(abs(dist_between_two(lat1,lng1,lat2,lng2)))

    num = best.index(max(best))

    key_list = list(places)
    name = key_list[num]

    return(name)