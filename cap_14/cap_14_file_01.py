# Data analysis with Pandas

import os
import pandas
print(os.listdir("files"))

df1 = pandas.read_csv("files/supermarkets.csv")
print(df1)

df2 = pandas.read_json("files/supermarkets.json")
print(df2)

df3 = pandas.read_excel("files/supermarkets.xlsx", sheet_name =0)
print(df3)

df4 = pandas.read_csv("files/supermarkets-commas.txt")
print(df4)

df5 = pandas.read_csv("files/supermarkets-semi-colons.txt", sep=";")  # default delimiter is ','
print(df5)

df6 = pandas.read_csv("files/data.txt", header=None)
print(df6)

df6.columns = ["ID(col1)", "Address(col2)", "City(col3)", "Zip(col4)", "Country(col5)", "Name(col6)", "Employees(col7)"]
print(df6)

print(df6.set_index("ID(col1)"))  # this method produces a new data frame on the fly, the original df6 will remain the same
print(df6)

df7 = df6.set_index("ID(col1)")  # assigning the set_index to a new variable will create a permanent DF with the new index
print(df7)

df8 = pandas.read_csv("files/data.txt")
print(df8)

df8.columns = ["ID(col1)", "Address(col2)", "City(col3)", "Zip(col4)", "Country(col5)", "Name(col6)", "Employees(col7)"]
print(df8)
df8.set_index("ID(col1)", inplace=True)
print(df8)