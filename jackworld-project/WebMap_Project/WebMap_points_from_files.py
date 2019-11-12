import folium
import pandas


voldata = pandas.read_csv('app2-web-map/Volcanoes.txt')
# print(voldata)
#
# print(voldata['LAT'],voldata['LON'])

# Want to create two different lists of the datapoints
lat = list(voldata['LAT'])
lon = list(voldata['LON'])
names = list(voldata['NAME'])
elev = list(voldata['ELEV'])


# one way is to turn the lat:long into into dictionary
# voldict = dict(zip(lat,lon))
# the issue is that you lose that capacity to iterate on the for loop

map = folium.Map()

vm = folium.FeatureGroup(name='VolcanoMap')
# vm.add_child(folium.Marker(location=[0,0], popup='VolName', icon=folium.Icon(color='green')))

def elevation_color(x):
    if x < 1000:
        return 'green'
    elif 1000 < x < 3000:
        return 'orange'
    else:
        return 'red'

# help(folium.CircleMarker)

#INSTEAD USE A ZIP TO ITERATE!!

for lat, lon, name, el in zip(lat, lon, names, elev):
    vm.add_child(folium.Marker(location=(lat, lon), radius=5, popup=name+', '+str(el), icon=folium.Icon(color=elevation_color(el))))
    map.add_child(vm)


# LOADING POLYGONS VIA GEOJSON
# GEOJSONS POLYGONS ARE DICTIONARIES
# https://en.wikipedia.org/wiki/GeoJSON
# adding Json as a child

#adding style_function: expects a lambda function
# ['properties']['POP2005'] represent a value within value within a value of the json
vm.add_child(folium.GeoJson(data=open('app2-web-map/world.json', 'r', encoding='UTF-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green'
                            if x['properties']['POP2005'] < 10000000 else 'yellow'}))





map.save('volc_map.html')