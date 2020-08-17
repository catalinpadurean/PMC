#Second application from PMC. Building Webmap with python and Folium
import folium
#print(dir(folium)) #get a list of available objects from Folium
#help(folium.Map) #help on folium.Map object 

#Create map object
map = folium.Map(location =[80,-100]) #list of coordinates, latitude from -90 to 90 and longitude from -180 to 180
print(map)
map.save("Map1.html")

jascau = folium.Map(location = [46.28, 22.28], zoom_start = 12)
jascau.save("Jascau.html")