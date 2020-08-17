"""Interacting with databases - SQLite(sqlite3) and PostgreSQL(psycopg2)"""
#sqlite3 is a library used to interact with SQLite database

#Interacting with a database in 5 steps:
#1.Connect to a database
#2.Create a cursor object
#3.Write an SQL query
#4.Commit changest
#5.Close connection

import sqlite3

def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert_value_table(item, quant, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    #A good practice when passing params is to use question marks and then specifiy which variables will replace the question marks
    #Using placeholders will make the code prone to SQL injections for mockers 
    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item, quant, price))
    connection.commit()
    connection.close()

#insert_value_table("Wate Glass", 10, 5)
#insert_value_table("Water Glass", 10, 5)
#insert_value_table("Coffe cup", 2, 2)

def view_data_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

def remove_value_table(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(item,)) #put a comma if you have only one parameter that needs to be replaced
    connection.commit()
    connection.close()

def update_value_table(quant, price, item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quant, price, item))
    connection.commit()
    connection.close()

#print(view_data_table())
#remove_value_table("Wate Glass")
#print(view_data_table())
update_value_table(5, 33.4, "Water Glass")
print(view_data_table())