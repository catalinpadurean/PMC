# Data analysis with Pandas

import pandas
import os

print(os.listdir("files"))

df9 = pandas.read_json("files/supermarkets.json")
print(df9)

df9 = df9.set_index("Address")
print(df9)

print(df9.loc["735 Dolores St":"332 Hill St", "Country":"ID"])  # check method parameters for better documentation
print(df9.loc["332 Hill St", "Country"])
# The preferred method to slice dataframes is by indexing "iloc" method
print(df9.iloc[1:3, 1:4])  # two parameters: 1st - range of indexes || 2nd range of columns)


#######################################################################################################################
