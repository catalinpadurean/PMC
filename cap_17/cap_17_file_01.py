#For this part of the chapter use tiles="Stamen Terrain" instead of "Mapbox Bright"
#They are both types of basemaps but Mapbox Bright does not work anymore
import folium
import pandas

map = folium.Map(location = [33.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain") #list of coordinates, latitude from -90 to 90 and longitude from -180 to 180

#TODO: START - >the best way to add a child to a map is to use a FeatureGrup
fg = folium.FeatureGroup(name = "My map")
fg.add_child(folium.Marker(location = [39.2, -99.1], popup = "Marker from FG is here", icon = folium.Icon(color = 'green')))
map.add_child(fg)
#TODO: END

#1.Adding multiple markers can be done with a for loop
coordinates_list = [[38.9, -99.5], [39.2, -100], [39, -101]]
coordinates_color = ['orange', 'gray', 'pink']
coordinates_text = ['Mk1', 'Mk2', 'Mk3'] 
for index in range(0, len(coordinates_list)):
    fg.add_child(folium.Marker(location = coordinates_list[index], popup = coordinates_text[index], icon = folium.Icon(color = coordinates_color[index])))

"""CODE BELOW CAN BE USED. WHEN I FIRST WROTE THIS PART I DID NOT KNOW ABOUT ZIP METHOD """    
#for coord_idx, pop_idx, color_idx in zip(coordinates_list, coordinates_text, coordinates_color):
#    fg.add_child(folium.Marker(location = coord_idx, popup = pop_idx, icon = folium.Icon(color = color_idx)))  
map.add_child(folium.Marker(location = [38.2, -99.1], popup = "Marker is here", icon = folium.Icon(color = 'red')))
#help(folium.Marker()) for information about Marker function
map.save("Map_X.html")

#2.Adding markers from files
#needing pandas for this part so install pandas if you haven't done it until now

map = folium.Map(location = [40.58, -29.09], zoom_start = 6, tiles = "Stamen Terrain") #list of coordinates, latitude from -90 to 90 and longitude from -180 to 180
fg_1 = folium.FeatureGroup(name = "My map")
data = pandas.read_csv("Volcanoes.csv")


#print(data.columns) use this to see the name of the columns available in data object
#based on previous print statement extract latitude and longitude from data file object 
lat = list(data["LAT"])
lon = list(data["LON"])
#print(lat) #if you want to see how the list will look like
#print(lon) #if you want to see how the list will look like

#use zip method to parse multiple lists at the same time. Use a specific index for each list
#this can be applied to the previous part where I used the index in range. That code could look like 
#TODO: for coord_idx, pop_idx, color_idx in zip(coordinates_list, coordinates_text, coordinates_color):
#TODO:    fg.add_child(folium.Marker(location = coord_idx, popup = pop_idx, icon = folium.Icon(color = color_idx)))  
for lt, ln in zip (lat, lon):
    fg_1.add_child(folium.Marker(location = [lt, ln], popup = "Marker from for loop using CSV", icon = folium.Icon(color = "lightblue")))
map.add_child(fg_1)

#print(data) just for test. Remove # if you want to see how the data from this file looks
map.save("Map_Y.html")

#3.Adding dynamic popup
map = folium.Map(location = [33.58, -97.09], zoom_start = 6, tiles = "Stamen Terrain") #list of coordinates, latitude from -90 to 90 and longitude from -180 to 180
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
fg_2 = folium.FeatureGroup(name = "My map")

for lt, ln, el in zip (lat, lon, elev):
    fg_2.add_child(folium.Marker(location = [lt, ln], popup = str(el) + " meters", icon = folium.Icon(color = "lightblue")))
#NOTE: if there are quotes in the string we might get a blank webpage. To avoid this issue you can use popup = folium.Popup(str(el), parse_html = True)
map.add_child(fg_2)

map.save("Map_Z.html")


#4.Color points
#Adding information to the popup. In this case we will change the color of the popup depending on the height of the volcano
def color_producer(elevation):
    if elevation < 1000 :
        return 'green'
    elif 1000 <= elevation < 3000 :
        return 'orange'
    else:
        return 'red'
    
map = folium.Map(location = [33.58, -97.09], zoom_start = 6, tiles = "Stamen Terrain") 
fg_3 = folium.FeatureGroup(name = "My map")
for lt, ln, el in zip (lat, lon, elev):
    fg_3.add_child(folium.Marker(location = [lt, ln], popup = str(el) + " meters", icon = folium.Icon(color = color_producer(el))))

map.add_child(fg_3)

map.save("Map_W.html")

#4.Change the shape of marker
map = folium.Map(location = [33.58, -97.09], zoom_start = 6, tiles = "Stamen Terrain") 
fg_4 = folium.FeatureGroup(name = "My map")

for lt, ln, el in zip (lat, lon, elev):
    fg_4.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = str(el) + " meters", fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

map.add_child(fg_4)

map.save("Map_X1.html")