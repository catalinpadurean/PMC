"""Object Oriented Programming explained"""
#Organizing the backend and frontend from PMC_app4 into OOP classes and 'style'
#Compare this file to PMC_app4.py to see the changes that were made

"""Frontend script to OOP"""

from cap_23_file_00 import Database
from tkinter import *

#Create a Database object
database = Database("books.db")

#Define frontend functions which will get the tuples returned by the backend functions
#This functions will be wrappers for backend functions
#A reason why we use wrapper functions is that when we developed backend functions some of them had parameters and when we are assigning a function to Tkinter widget we can't use brackets and params so we will assign the wrapper function and handle the parameters inside of the wrapper

class Interface(object):
    


    def __init__(self, window):
        
        #Create main window
        self.main_window = window    
        self.main_window.wm_title("BookStoreApp")
        #TODO: try to add some 'features' to the window and also learn more about TK

        #Create the  labels
        self.lb1 = Label(self.main_window, text="Title")
        self.lb1.grid(row = 0, column = 0)

        self.lb2 = Label(self.main_window, text="Author")
        self.lb2.grid(row = 0, column = 2)

        self.lb3 = Label(self.main_window, text="Year")
        self.lb3.grid(row = 1, column = 0)

        self.lb4 = Label(self.main_window, text="ISBN")
        self.lb4.grid(row = 1, column = 2)

        #Create the entries
        self.title_value = StringVar()
        self.en1_title = Entry(self.main_window, textvariable = self.title_value)
        self.en1_title.grid( row = 0, column = 1)

        self.author_value = StringVar()
        self.en2_author = Entry(self.main_window, textvariable = self.author_value)
        self.en2_author.grid( row = 0, column = 3)

        self.year_value = StringVar()
        self.en3_year = Entry(self.main_window, textvariable = self.year_value)
        self.en3_year.grid( row = 1, column = 1)

        self.isbn_value = StringVar()
        self.en4_isbn = Entry(self.main_window, textvariable = self.isbn_value)
        self.en4_isbn.grid( row = 1, column = 3)

        #Create the listbox
        self.lstb1 = Listbox(self.main_window, height = 6, width = 60)
        self.lstb1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

        #Create the scrollbar
        self.sb1 = Scrollbar(self.main_window)
        self.sb1.grid(row = 2, column = 2, rowspan = 6)

        #Connect the listbox to the scrollbar
        self.lstb1.configure(yscrollcommand =self.sb1.set)
        self.sb1.configure(command = self.lstb1.yview)

        #Bind an widget event to a function. In this case, we will bind the selected line from the ListBox to delete function
        self.lstb1.bind('<<ListboxSelect>>', self.get_selected_row)
        
        
        #Create the buttons
        bt1_view_all = Button(self.main_window, text = "View all", width = 12, command = self.view_command)
        bt1_view_all.grid(row = 2, column =3)

        bt2_search = Button(self.main_window, text = "Search entry", width = 12, command = self.search_command)
        bt2_search.grid(row = 3, column =3)

        bt3_add = Button(self.main_window, text = "Add entry", width = 12, command = self.add_command)
        bt3_add.grid(row = 4, column =3)

        bt4_update = Button(self.main_window, text = "Update entry", width = 12, command = self.update_command)
        bt4_update.grid(row = 5, column =3)

        bt5_delete = Button(self.main_window, text = "Delete entry", width = 12, command = self.delete_command )
        bt5_delete.grid(row = 6, column =3)

        bt6_close = Button(self.main_window, text = "Close", width = 12, command = self.main_window.destroy)
        bt6_close.grid(row = 7, column =3)

    #Create get_selected_row function used for binding the listbox selection
    def get_selected_row(self, event): #This function will get a different type of param: event
        try:
            index = self.lstb1.curselection()[0]
            self.selected_tuple = self.lstb1.get(index) #From the listbox get the tuple with the index X
            #Using the global variable in this function allows us to skip the return part of the function.
            
            #Add the values of the selected row into the entries
            self.en1_title.delete(0,END)
            self.en1_title.insert(END, self.selected_tuple[1])

            self.en2_author.delete(0,END)
            self.en2_author.insert(END, self.selected_tuple[2])

            self.en3_year.delete(0,END)
            self.en3_year.insert(END, self.selected_tuple[3])

            self.en4_isbn.delete(0,END)
            self.en4_isbn.insert(END, self.selected_tuple[4])
        except IndexError: #If the user clicks the listbox when the list in empty, the selected_tuple will be empty 
            pass


    #Create a view function for "view_db"
    def view_command(self):
        self.lstb1.delete(0,END)
        for row in database.view_db():
            self.lstb1.insert(END,row) #TODO: try to use enumerate and pass the counter and row to insert function. Just an ideea

    #Create a search function for "search_db"
    def search_command(self):
        self.lstb1.delete(0,END) #TODO: Give the user the option to enter just a word from author or title and show all books that contain the word in the author name or book title
        #Iterate through the search_db function. Use the StringVar().get() method for getting the string inside of each entry and pass it as a parameter for the backend function
        for row in database.search_db(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()):
            self.lstb1.insert(END, row)

    #Create an add function for "insert_db"
    def add_command(self):
        database.insert_db(self.title_value.get(), self.author_value.get(),self.year_value.get(), self.isbn_value.get())
        self.lstb1.delete(0,END)
        self.lstb1.insert(END,(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()))
        #TODO: Check if the current entry does not exist already(Author, Name, ISBN should be the most important to check)
        #TODO2: Clear the entry widgets after the execution

    #Create a delete function for "delete_db"
    def delete_command(self):
        database.delete_db(self.selected_tuple[0])
        #Pass only the id of the entry in the database
        #Using the global variable will allow us to use the tuple from the backend without calling the get_selected_row function inside this function
        #TODO: Refresh the listbox after deletion

    #Create an update function for "update_db"
    def update_command(self):
        database.update_db(self.selected_tuple[0], self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        #TODO: Refresh the listbox after update

window = Tk()
Interface(window)
window.mainloop()