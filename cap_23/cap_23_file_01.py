"""Object Oriented Programming explained"""
#Organizing the backend and frontend from PMC_app4 into OOP classes and 'style'


"""Frontend script to OOP"""

from cap_23_file_00 import Database
from tkinter import *

#Create a Database object
database = Database("books.db")

#Define frontend functions which will get the tuples returned by the backend functions
#This functions will be wrappers for backend functions
#A reason why we use wrapper functions is that when we developed backend functions some of them had parameters and when we are assigning a function to Tkinter widget we can't use brackets and params so we will assign the wrapper function and handle the parameters inside of the wrapper

#Create get_selected_row function used for binding the listbox selection
def get_selected_row(event): #This function will get a different type of param: event
    try:
        global selected_tuple #Create a global variable for storing the tupple from the listbox and also to pass as a parameter to the backend function
        index = lstb1.curselection()[0]
        selected_tuple = lstb1.get(index) #From the listbox get the tuple with the index X
        #Using the global variable in this function allows us to skip the return part of the function.
        
        #Add the values of the selected row into the entries
        en1_title.delete(0,END)
        en1_title.insert(END, selected_tuple[1])

        en2_author.delete(0,END)
        en2_author.insert(END, selected_tuple[2])

        en3_year.delete(0,END)
        en3_year.insert(END, selected_tuple[3])

        en4_isbn.delete(0,END)
        en4_isbn.insert(END, selected_tuple[4])
    except IndexError: #If the user clicks the listbox when the list in empty, the selected_tuple will be empty 
        pass


#Create a view function for "view_db"
def view_command():
    lstb1.delete(0,END)
    for row in database.view_db():
        lstb1.insert(END,row) #TODO: try to use enumerate and pass the counter and row to insert function. Just an ideea

#Create a search function for "search_db"
def search_command():
    lstb1.delete(0,END) #TODO: Give the user the option to enter just a word from author or title and show all books that contain the word in the author name or book title
    #Iterate through the search_db function. Use the StringVar().get() method for getting the string inside of each entry and pass it as a parameter for the backend function
    for row in database.search_db(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        lstb1.insert(END, row)

#Create an add function for "insert_db"
def add_command():
    database.insert_db(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    lstb1.delete(0,END)
    lstb1.insert(END,(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))
    #TODO: Check if the current entry does not exist already(Author, Name, ISBN should be the most important to check)
    #TODO2: Clear the entry widgets after the execution

#Create a delete function for "delete_db"
def delete_command():
    database.delete_db(selected_tuple[0])
    #Pass only the id of the entry in the database
    #Using the global variable will allow us to use the tuple from the backend without calling the get_selected_row function inside this function
    #TODO: Refresh the listbox after deletion

#Create an update function for "update_db"
def update_command():
    database.update_db(selected_tuple[0], title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    #TODO: Refresh the listbox after update
#Create main window
main_window = Tk()
main_window.wm_title("BookStoreApp")
#TODO: try to add some 'features' to the window and also learn more about TK

#Create the  labels
lb1 = Label(main_window, text="Title")
lb1.grid(row = 0, column = 0)

lb2 = Label(main_window, text="Author")
lb2.grid(row = 0, column = 2)

lb3 = Label(main_window, text="Year")
lb3.grid(row = 1, column = 0)

lb4 = Label(main_window, text="ISBN")
lb4.grid(row = 1, column = 2)

#Create the entries
title_value = StringVar()
en1_title = Entry(main_window, textvariable = title_value)
en1_title.grid( row = 0, column = 1)

author_value = StringVar()
en2_author = Entry(main_window, textvariable = author_value)
en2_author.grid( row = 0, column = 3)

year_value = StringVar()
en3_year = Entry(main_window, textvariable = year_value)
en3_year.grid( row = 1, column = 1)

isbn_value = StringVar()
en4_isbn = Entry(main_window, textvariable = isbn_value)
en4_isbn.grid( row = 1, column = 3)

#Create the listbox
lstb1 = Listbox(main_window, height = 6, width = 60)
lstb1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

#Create the scrollbar
sb1 = Scrollbar(main_window)
sb1.grid(row = 2, column = 2, rowspan = 6)

#Connect the listbox to the scrollbar
lstb1.configure(yscrollcommand = sb1.set)
sb1.configure(command = lstb1.yview)

#Bind an widget event to a function. In this case, we will bind the selected line from the ListBox to delete function
lstb1.bind('<<ListboxSelect>>', get_selected_row)
#Create the buttons
bt1_view_all = Button(main_window, text = "View all", width = 12, command = view_command)
bt1_view_all.grid(row = 2, column =3)

bt2_search = Button(main_window, text = "Search entry", width = 12, command = search_command)
bt2_search.grid(row = 3, column =3)

bt3_add = Button(main_window, text = "Add entry", width = 12, command = add_command)
bt3_add.grid(row = 4, column =3)

bt4_update = Button(main_window, text = "Update entry", width = 12, command = update_command)
bt4_update.grid(row = 5, column =3)

bt5_delete = Button(main_window, text = "Delete entry", width = 12, command = delete_command )
bt5_delete.grid(row = 6, column =3)

bt6_close = Button(main_window, text = "Close", width = 12, command = main_window.destroy)
bt6_close.grid(row = 7, column =3)

#Call mainloop so that we wrap up all the widgets
main_window.mainloop()
