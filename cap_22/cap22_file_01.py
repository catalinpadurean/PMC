"""Building a real world program, database for books. We will also build an executable file """

#We will use tkinter for GUI and sqlite3 for database (addapt for PostgreSQL as well)
#Before starting the work on frontend|backend first we must clarify the requirements
""" 
This app will store book information: Title, Author, Year, ISBN
The user can:
- view all records
- search an entry
- add an entry
- update an entry
- delete an entry
- close
"""
#There is no specific order to start a fullstack dev project.

"""BACKEND DEVELOPEMNT OF THE APP"""

import sqlite3

#Create functions for database manipulation acording to the buttons designed in the frontend script(cap22_file_00.py)

#Create a connection to a database
def connect_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

#Create an insert function
def insert_db(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)",(title,author,year, isbn)) #NULL is used because we don't want to enter a primary key, if we pass NULL the primary key will be automatically created
    connection.commit()
    connection.close()

#Create an view function
def view_db():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    connection.close()

    return rows

#Create an OR search function where the user can search in the database using one OR multiple search criterias
def search_db(title="", author="", year="", isbn=""):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?",(title, author, year, isbn))
    rows = cursor.fetchall()
    connection.close()
    
    return rows

#Create a delete record function. The user will select an entry from the listbox of the GUI and the entry will be deleted
#The deletion will be based on the ID of the entry because the ID is the primary key of the database
def delete_db(id):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?",(id, ))
    connection.commit()
    connection.close()

#Create an update record function. The user will select an entry from the listbox of the GUI and the values of the entry will be displayed in the textboxes of the GUI
#The user will update the textboxes(entries) and the database will be updated
def update_db(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
    connection.commit()
    connection.close()

#Call connect_db to run everytime we run the cap22_file_01.py (BACKEND)
#cap22_file_01.py will be imported in the frontend script(cap22_file_00.py)
connect_db()

#Test code
#insert_db("Teoria Universala2", "Stephen Hawking", 2019, 97897350)
#insert_db("Teoria Universala3", "Stephen Hawking", 2029, 12097350)
#insert_db("The Big Picture", "Sean Carroll", 2016, 97224410)
#insert_db("Pamantul e plat", "Alex Dopplegengar", 2019, 93245209)
#print(view_db())
#print(search_db(title="Pamantul e plat"))
#delete_db(5)
print(view_db())
update_db(6, "Teoria Universala_3", "S.Hawk", 2020, 66666350)
print(view_db())