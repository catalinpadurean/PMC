#Map with folium
import folium
import pandas

def color_producer(elevation):
    if elevation < 1000 :
        return 'green'
    elif 1000 <= elevation < 3000 :
        return 'orange'
    else:
        return 'red'

#Create map object
map = folium.Map(location = [33.58, -97.09], zoom_start = 6, tiles = "Stamen Terrain") 

#Read volcanoes.csv file and create lists with needed information
volc_data = pandas.read_csv("Volcanoes.csv")

volc_lat = list(volc_data["LAT"])
volc_lon = list(volc_data["LON"])
volc_elev = list(volc_data["ELEV"])
volc_type = list(volc_data["TYPE"])
#Read capitals.txt file and create lists with needed information
countries_data = pandas.read_csv("capitals.txt")

country_lat = list (countries_data["Latitude"])
country_lon = list (countries_data["Longitude"])
country_name = list(countries_data["Country"])
country_city = list(countries_data["Capital"])

#Create a feature group for volcanoes.
#Add the volcanoes on the map with: circle markers, different color based on height(elevation, popup message that will show Type and Height)

volc_fg = folium.FeatureGroup("Volcanoes Information")
for lt, ln, el, tp in zip( volc_lat, volc_lon, volc_elev, volc_type):
    volc_fg.add_child(folium.CircleMarker( location = [lt, ln], radius = 9, popup = folium.Popup("Height: " +str(el) +" m" + "\n" + "Type: " +str(tp), parse_html = True), fill_color = color_producer(el), color = 'black', fill_opacity = 0.9))
map.add_child(volc_fg)

#Create a feature group for the capitals
#Add capitals on the map with: normal markers, popup message will show "X is capital of Y"

country_fg = folium.FeatureGroup("Capitals Information")
for lt, ln, nm, ct in zip(country_lat, country_lon, country_name, country_city):
    country_fg.add_child(folium.Marker(location = [lt, ln], popup = ct + " is CAP of " + nm, icon = folium.Icon(color = "lightblue", icon_color = 'white' ), tooltip="Click me!"))
map.add_child(country_fg)

#Add polygon on the map. Use the world.json file to highlight each country and change the color of the country based on population
polygon_fg = folium.FeatureGroup("Polygon Information")
#using a lambda function (expected as a parameter for style_function) to add diferent colors to polygons depending on the population
#the lambda will create a dictionary
#use x from lambda to parse the data from the file, get the value of the POP2005 atribute of the 'properties' atribute from the  world.json file
polygon_fg.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 50000000 else 'white' if 5000000 <= x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 15000000 else 'red' if 15000000 <= x['properties']['POP2005'] < 20000000 else 'black'}))
map.add_child(polygon_fg)

#Add layer control panel
map.add_child(folium.LayerControl())

#Save the map
map.save("ApplicationMap.html")