import mapbox

def distanca(mesto):
    destination = str(mesto) + ', Serbia'
    map = mapbox.Geocoder(access_token="pk.eyJ1IjoiZHVoaXpqYW1lIiwiYSI6ImNrZHhzdGxvbDM0aGkyd21xNHVleTByajUifQ.esMht2IXyPcuICHLA9vl2Q")
    d_code = map.forward(destination)
    dest = d_code.json()
    for z in dest['features']:
        print(z)
        print("============================================")
    beograd = map.forward("Belgrade, Serbia")

    bg_json = beograd.json()
    
    destination = {
        'type': 'Feature',
        'properties': {'name': destination},
        'geometry': {
            'type': 'Point',
            'coordinates': dest['features'][0]['center']
            }
        }
    service = mapbox.Directions(access_token="pk.eyJ1IjoiZHVoaXpqYW1lIiwiYSI6ImNrZHhzdGxvbDM0aGkyd21xNHVleTByajUifQ.esMht2IXyPcuICHLA9vl2Q")
    
    origin = {
            'type': 'Feature',
            'properties': {'name': "Belgrade, Serbia"},
            'geometry': {
                'type': 'Point',
                'coordinates': bg_json['features'][0]['center']
                }
            }
    directions = service.directions([origin,destination])
    dir_json = directions.json()
    distance = dir_json['routes'][0]['legs'][0]['distance']/1000
    print(distance)
        # if distance < 165 and place[0] == 'Belgrade':
        #     return True
        # if distance < 60 and place[0] == 'Novi Sad':
        #     return True
        # if distance < 80 and place[0] == 'Lazarevac':
        #     return True
        # return False

mesto = str(input("Unesite mesto: "))
distanca(mesto)