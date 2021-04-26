import mapbox
import json

map = mapbox.Geocoder(access_token="pk.eyJ1IjoiZHVoaXpqYW1lIiwiYSI6ImNrZHhzdGxvbDM0aGkyd21xNHVleTByajUifQ.esMht2IXyPcuICHLA9vl2Q")
code = map.forward("Kladovo, Serbia")
code2 = map.forward("Novi Sad, Serbia")
# print(code)
kod = code.json()
kod2 = code2.json()
print(kod['features'][0]['center'])
# print(kod)
service = mapbox.Directions(access_token="pk.eyJ1IjoiZHVoaXpqYW1lIiwiYSI6ImNrZHhzdGxvbDM0aGkyd21xNHVleTByajUifQ.esMht2IXyPcuICHLA9vl2Q")
origin = {
        'type': 'Feature',
        'properties': {'name': 'Kladovo, Serbia'},
        'geometry': {
            'type': 'Point',
            'coordinates': kod['features'][0]['center']
            }
        }
destination = {
'type': 'Feature',
'properties': {'name': 'Novi Sad, Serbia'},
'geometry': {
    'type': 'Point',
    'coordinates': kod2['features'][0]['center']
    }
}


place = service.directions([origin,destination])
x = place.json()
print(x['routes'][0]['legs'][0]['distance']/1000)
