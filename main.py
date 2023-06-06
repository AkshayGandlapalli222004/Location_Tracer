import phonenumbers
import folium
#To determine the country in which the phone number is located:
from local1 import a
from phonenumbers import geocoder
country=phonenumbers.parse(a)
location=geocoder.description_for_number(country,"en")
print(location)

Key= "8a0e8f06fece4e11adef12a365ab9be3"
#To determine the service provider of that particular number:
from phonenumbers import carrier
service_provider=phonenumbers.parse(a)
d=carrier.name_for_number(service_provider,"en")
print(d)

from opencage.geocoder import OpenCageGeocode
geocoder =OpenCageGeocode(Key)
query=str(location)
results=geocoder.geocode(query)
#print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)


my=folium.Map(location=[lat,lng],zoom_start = 10)
folium.Marker([lat,lng],popup=location).add_to(my)
my.save("My_Location.html")