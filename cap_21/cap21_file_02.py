"""Interacting with databases - SQLite(sqlite3) and PostgreSQL(psycopg2)"""
#psycopg2 is a librabry used to interact with PostgreSQL(both of them need to be installed)
#We will use mainly the script written in the cap21_file_01 and adjust it for psycopg2
import psycopg2

#use pgAdmin to create a new table or use the existing one
#in pyscopg2 we can't use question mark and we will use %s
def create_table():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='fabregas4' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert_value_table(item, quant, price):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='fabregas4' host='localhost' port='5432' ")
    cursor = connection.cursor()
    #A good practice when passing params is to use question marks and then specifiy which variables will replace the question marks
    #Using placeholders will make the code prone to SQL injections for mockers 
    #cursor.execute("INSERT INTO store VALUES(?,?,?)",(item, quant, price)) - used in sqlite3
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quant, price))
    connection.commit()
    connection.close()

def view_data_table():
    connection = psycopg2.connect("dbname='database1' user='postgres' password='fabregas4' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

def remove_value_table(item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='fabregas4' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s",(item,)) #put a comma if you have only one parameter that needs to be replaced
    connection.commit()
    connection.close()

def update_value_table(quant, price, item):
    connection = psycopg2.connect("dbname='database1' user='postgres' password='fabregas4' host='localhost' port='5432' ")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quant, price, item))
    connection.commit()
    connection.close()

create_table()
#insert_value_table("Apple", 20, 100.5)
insert_value_table("Orange", 10, 20.5)
print(view_data_table())
#remove_value_table('Orange')
#print(view_data_table())
update_value_table(5, 2000, "Apple")
print(view_data_table())