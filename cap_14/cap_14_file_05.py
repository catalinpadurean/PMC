#######################################################################################################################

# We are going to use Nominatim() in the next video. Nominatim() currently has a bug. To fix this problem, whenever you see these lines in the next video:

# from geopy.geocoders import Nominatim
# nom = Nominatim()
# change them to these

# from geopy.geocoders import ArcGIS
# nom = ArcGIS()
# The rest of the code remains the same.

#######################################################################################################################

# The process of converting from addresses to coordinates ->geocoding
import pandas
import os
import geopy

from geopy.geocoders import ArcGIS as arcgis

os.listdir("files")
df12 = pandas.read_csv("files/supermarkets.csv")
print(df12)
print(dir(geopy))

nom = arcgis()
print(nom.geocode("3995 23rd St, San Francisco, CA 94114"))
n = nom.geocode("3995 23rd St, San Francisco, CA 94114")

print("Type of nom.geocode is: ", type(n))
print("______________________________________________________________________________________________________________")
print("Show latitude and longitude of geocode object: \n")
print("Latitude: ", n.latitude)
print("Longitude: ", n.longitude)
print("______________________________________________________________________________________________________________")
print("Add new columns in dataframe to prepare address for geocode")
df12["Address"] = df12["Address"] + ", " + df12["City"]+ ", "+df12["State"]+", "+df12["Country"]
print(df12)
df12["Coordinates"] = df12["Address"].apply(nom.geocode)
print(df12)
print("______________________________________________________________________________________________________________")
print("Coordinates column: ")
print(df12.Coordinates)
print("First entry from coordinates column: ")
print(df12.Coordinates[0])
print("Latitude of first entry: ")
print(df12.Coordinates[0].latitude)
print("______________________________________________________________________________________________________________")
print("Add Latitude and Longitude columns by applying latitude and longitude atributes from geocode to entire series")
df12["Latitude"] = df12["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
df12["Longitude"] = df12["Coordinates"].apply(lambda x: x.longitude if x is not None else None)
print("______________________________________________________________________________________________________________")
print("Show final DF")
print(df12)
