import googlemaps
import pprint
import time
#from GoogleMapsAPIKey import get_my_key
#from Auto_search import ready()

#cords = ready()
cords = '-33.8670522,151.195362'


def locations(cords):
	#API_KEY = get_my_key()
	API_KEY = 'AIzaSyCndiwpn0s7MRo2qbhPbzhSxdODyPkFDBo'
	gmaps = googlemaps.Client(key = API_KEY)
	#define search
	places_result = gmaps.places_nearby(location = cords, radius = 200, open_now = False, type = 'parking')
	parkings = dict()
	#loop through places_nearby
	for place in places_result['results']:
		my_place_id = place['place_id']
		
		my_fields = ['formatted_address','name','opening_hours', 'formatted_phone_number','photo']
		
		#make request
		place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
		
		
		#pprint.pprint(place_details)
			
		
	return place_details

pprint.pprint(locations(cords))
