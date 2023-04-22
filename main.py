from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app_name")
location = geolocator.geocode("ul. Mickiewicza 9, Warszawa, Polska", headers={'User-Agent': 'Mozilla/5.0'})
print((location.latitude, location.longitude))