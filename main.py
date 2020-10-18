import googlemaps
import random

MINIMUM_RATING = 4
VENUE_TYPE = 'bar'  # `bar` or `restaurant`
OPEN_NOW = False
MAX_RADIUS_METERS = 800

gmaps = googlemaps.Client(key='YOUR_API_KEY')

# ADD YOUR LAT /LNG HERE
location = (lat, lng)

nearby_places = gmaps.places_nearby(
    location=location, name=VENUE_TYPE, open_now=OPEN_NOW, radius=MAX_RADIUS_METERS
)['results']

choices = []
for nearby_place in nearby_places:
    if nearby_place['rating'] > MINIMUM_RATING:
        choices.append(nearby_place)

selected_place = random.choice(choices)

print("You are going to .. .. .. ..")
print(selected_place['name'])
print(selected_place['vicinity'])
print("Rated: {} with {} reviews".format(selected_place['rating'], selected_place['user_ratings_total']))
