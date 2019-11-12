import folium

# Create a map object and default location
# you can add a zoom parameter - zoom_start
# you can add styles
map = folium.Map(location=[38.58, -99.89], zoom_start=6, tiles='Stamen Terrain')

# help(folium.Map)

# Create a default location

# ADDING MARKERS
# Check folium directory
# objects added to the map are referred to as children, use th add_child method
# markers need locations just like the center map
# add popup titles with popup and icon style with icon method


# Use the feature group method to save custom map styles
fg = folium.FeatureGroup(name='MyMap')
fg.add_child(folium.Marker(location=[38.2, -99.1], popup='Hi Im a marker', icon=folium.Icon(color='green')))
map.add_child(fg)

#Adding multiple markers

fg2 = folium.FeatureGroup(name='MyMap2')
x = 38
for x in range(0,38):
    fg2.add_child(folium.Marker(location=[x, -99.1], popup='Hi Im a marker', icon=folium.Icon(color='green')))
    x += 1
    map.add_child(fg2)

# You can also iterate through a list of lists

for coordinates in [[38.2, -96.1], [38.2, -95.1], [38.2, -94.1]]:
    fg2.add_child(folium.Marker(location=coordinates, popup='Hi Im a marker', icon=folium.Icon(color='green')))
    map.add_child(fg2)








map.save("activemap.html")