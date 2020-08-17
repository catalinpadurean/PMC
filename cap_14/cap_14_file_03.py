# Data analysis with Pandas

import pandas
import os

print(os.listdir("files"))

df10 = pandas.read_json("files/supermarkets.json")
print(df10)

df10.set_index("Address", inplace=True)

print(df10.drop("City", 1))  # drop method will not apply on the current dataframe but will create a new DF on the fly
print(df10.drop("332 Hill St", 0))  # the second argument can be 0 or 1. 1 for columns and 0 for index




