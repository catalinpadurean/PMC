"""Building a real world program, database for books. We will also build an executable file """

#We will use tkinter for GUI and sqlite3 for database 
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

"""FRONTEND DEVELOPEMNT OF THE APP"""
# Before starting the development of the GUI it is recommended to have a sketch of what the GUI will look like

from tkinter import *

#Create main window
main_window = Tk()

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
lstb1 = Listbox(main_window, height = 7, width =35)
lstb1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

#Create the scrollbar
sb1 = Scrollbar(main_window)
sb1.grid(row = 2, column = 2, rowspan = 6)

#Connect the listbox to the scrollbar
lstb1.configure(yscrollcommand = sb1.set)
sb1.configure(command = lstb1.yview)

#Create the buttons
bt1_view_all = Button(main_window, text = "View all", width = 12)
bt1_view_all.grid(row = 2, column =3)

bt2_search = Button(main_window, text = "Search entry", width = 12)
bt2_search.grid(row = 3, column =3)

bt3_add = Button(main_window, text = "Add entry", width = 12)
bt3_add.grid(row = 4, column =3)

bt4_update = Button(main_window, text = "Update entry", width = 12)
bt4_update.grid(row = 5, column =3)

bt5_delete = Button(main_window, text = "Delete entry", width = 12)
bt5_delete.grid(row = 6, column =3)

bt6_close = Button(main_window, text = "Close", width = 12)
bt6_close.grid(row = 7, column =3)

#Call mainloop so that we wrap up all the widgets
main_window.mainloop()
