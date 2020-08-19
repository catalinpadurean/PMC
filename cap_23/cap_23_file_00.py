"""Object Oriented Programming explained"""
#Organizing the backend and frontend from PMC_app4 into OOP classes and 'style'
#Compare this file to PMC_app4_bk.py to see the changes that were made

"""Backend script to OOP"""
import sqlite3

class Database:
    """Database class along with it's methods"""

    def __init__(self, db):
        #Constructor - This function is executed when the object is initialized
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connection.commit()

    #Create an insert function
    def insert_db(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)",(title,author,year, isbn)) #NULL is used because we don't want to enter a primary key, if we pass NULL the primary key will be automatically created
        self.connection.commit()

    #Create an view function
    def view_db(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()

        return rows

    #Create an OR search function where the user can search in the database using one OR multiple search criterias
    def search_db(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?",(title, author, year, isbn))
        rows = self.cursor.fetchall()
       
        return rows

    #Create a delete record function. The user will select an entry from the listbox of the GUI and the entry will be deleted
    #The deletion will be based on the ID of the entry because the ID is the primary key of the database
    def delete_db(self, id):
        self.cursor.execute("DELETE FROM book WHERE id=?",(id, ))
        self.connection.commit()

    #Create an update record function. The user will select an entry from the listbox of the GUI and the values of the entry will be displayed in the textboxes of the GUI
    #The user will update the textboxes(entries) and the database will be updated
    def update_db(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
        self.connection.commit()

    def __del__(self):
        #Destructor-this function will be called when the object  is destroyed
        self.connection.close()

