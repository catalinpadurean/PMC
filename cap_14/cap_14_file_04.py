# Data analysis with Pandas

import pandas
import os

print(os.listdir("files"))
df11 = pandas.read_json("files/supermarkets.json")
df11 = df11.set_index("Address")
print(df11)

# df11["Continent"]=["North America"] #check length of index and columns to correct this error
print(len(df11.index))
print(len(df11.columns))

print(df11.shape)
print(df11.shape[0])
df11["Continent"] = df11.shape[0]*["North America"]  # use the first value of df11.shape to create the length of data frame column filled with North America
print(df11)
df11["Continent"]=df11["Country"] + "," + "North America"  # update Continent column with values from Country + string "North America
print(df11)

df11_t = df11.T  # T is a method that transposes the DF
print(df11_t)

df11_t["My Address"]=["My_City", "My_Country", 10, 7 ,"My_Shop", "My_State", "My_Continent"]  # add a new column in the transposed data frame
print(df11_t)

df11 = df11_t.T  # retain in the original data frame, the transposing of the transposed and updated DF
print(df11)
