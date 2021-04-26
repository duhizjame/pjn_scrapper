import json
import mapbox
import sqlite3
def distanca(mesto):
    destination = str(mesto).replace('đ','dj') + ', Serbia'
    db = sqlite3.connect("placesDB.db")
    map = mapbox.Geocoder(access_token="pk.eyJ1IjoiZHVoaXpqYW1lIiwiYSI6ImNrZHhzdGxvbDM0aGkyd21xNHVleTByajUifQ.esMht2IXyPcuICHLA9vl2Q")
    d_code = map.forward(destination)
    dest = d_code.json()
    y = 0
    nasao = False 
    while(dest['features'][int(y)]['place_type']!=["place"] or dest['features'][int(y)]['place_type']!=["region"]  or dest['features'][int(y)]['text']=="Serbia"):
        for i,z in enumerate(dest['features']):
            if (z['place_type']==['place'] or z['place_type']==['region']) and z['text']!="Serbia":
                # print(z)
                y = i
                nasao = True
                break
        if nasao == True:
            break
        x = str(mesto).replace('đ','dj').replace('š','s').replace('ž','z').replace('č','c').replace('ć','c').replace('Đ','Dj').replace('Š','S').replace('Ž','Z').replace('Č','C').replace('Ć','C')
        execution = f"SELECT * from mesto where nazivMesta = \"{x}\""
        cursor = db.execute(execution)
        res = cursor.fetchone()
        print(res)
        if res is None:
            print("Can't find place in database.")
            return
        zipCode = res[0]
        while(zipCode % 100 !=0 ):
            zipCode = zipCode - 1
            cursor = db.execute(f"SELECT * from mesto where idMesta = {zipCode}")
            mesto = cursor.fetchone()
            print(mesto)
            if mesto is None:
                continue
            d_code = map.forward(str(mesto) + ', Serbia')
            dest = d_code.json()
            print(dest['features'][y]['text'])
            if (dest['features'][y]['place_type']==["place"] or dest['features'][int(y)]['place_type']==["region"]) and dest['features'][y]['text']!="Serbia":
                break
    beograd = map.forward("Belgrade, Serbia")
    novi_sad = map.forward("Novi Sad, Serbia")
    lazarevac = map.forward("Lazarevac, Serbia")

    bg_json = beograd.json()
    la_json = lazarevac.json()
    ns_json = novi_sad.json()

    origins = [] 
    origins.append((bg_json['features'][0]['text'],bg_json['features'][0]['center']))
    origins.append((la_json['features'][0]['text'],la_json['features'][0]['center']))
    origins.append((ns_json['features'][0]['text'],ns_json['features'][0]['center']))
    destinations = {
        'type': 'Feature',
        'properties': {'name': dest['features'][y]['text']},
        'geometry': {
            'type': 'Point',
            'coordinates': dest['features'][y]['center']
            }
        }
    service = mapbox.Directions(access_token="pk.eyJ1IjoiZHVoaXpqYW1lIiwiYSI6ImNrZHhzdGxvbDM0aGkyd21xNHVleTByajUifQ.esMht2IXyPcuICHLA9vl2Q")
    for place in origins: 
        origin = {
                'type': 'Feature',
                'properties': {'name': place[0]},
                'geometry': {
                    'type': 'Point',
                    'coordinates': place[1]
                    }
                }
        directions = service.directions([origin,destinations])
        dir_json = directions.json()
        distance = dir_json['routes'][0]['legs'][0]['distance']/1000
        print(distance,place[0])
        return (distance,place[0])


mesto = str(input("Unesite mesto: "))
distanca(mesto)