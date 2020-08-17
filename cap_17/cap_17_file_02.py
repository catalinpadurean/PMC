#Adding a new layer to the map. Currently we have 2 layers: base map & map tiles

import folium
import pandas

def color_producer(elevation):
    if elevation < 1000 :
        return 'green'
    elif 1000 <= elevation < 3000 :
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [33.58, -97.09], zoom_start = 6, tiles = "Stamen Terrain") 
data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

fg_5 = folium.FeatureGroup(name = "My map0")
for lt, ln, el in zip (lat, lon, elev):
    fg_5.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " meters", fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

#Adding a poligon layer
#GeoJson is another type of Json

fg_5.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read()))

map.add_child(fg_5)
map.save("Map_A1.html")

#Adding colors to poligons

fg_6 = folium.FeatureGroup(name = "My map1")
for lt, ln, el in zip (lat, lon, elev):
    fg_6.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " meters", fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

#using a lambda function (expected as a parameter for style_function) to add diferent colors to polygons depending on the population
#the lambda will create a dictionary
#use x from lambda to parse the data from the file, get the value of the POP2005 atribute of the 'properties' atribute from the  world.json file
fg_6.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_6)
map.save("Map_A2.html")

#Adding layer control panel 
fg_7 = folium.FeatureGroup(name = "My map 2")
for lt, ln, el in zip (lat, lon, elev):
    fg_7.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " meters", fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

#using a lambda function (expected as a parameter for style_function) to add diferent colors to polygons depending on the population
#the lambda will create a dictionary
#use x from lambda to parse the data from the file, get the value of the POP2005 atribute of the 'properties' atribute from the  world.json file
fg_7.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_7)
map.add_child(folium.LayerControl())
map.save("Map_A3.html")



#NOTE: it is better to use FeatureGroup when adding multiple markers on the map if we use also a Control Panel
#in the current example if we had used map.addchild instead of fg.add_child we would have 62 volcanoes layers in the control panel. Feature group is useful when adding a layer that contains multiple 'objects' of the same kind.