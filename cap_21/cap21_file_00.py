"""Interacting with databases - SQLite(sqlite3) and PostgreSQL(psycopg2)"""
#sqlite3 is a library used to interact with SQLite database

#Interacting with a database in 5 steps:
#1.Connect to a database
#2.Create a cursor object
#3.Write an SQL query
#4.Commit changest
#5.Close connection

import sqlite3

#1.Connect to a database
connection = sqlite3.connect("lite.db")
#2.Create a cursor object
cursor = connection.cursor()
#3.SQL code will be written as a string in the execute method. Use capital letters for SQL code
cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
cursor.execute("INSERT INTO store VALUES('Wine Glass', 8, 10.5)")
#4.Commit changes
connection.commit()
#5.Close connection
connection.close()
