"""Create a Python program that expects a kilogram input value and converts that value to grams, pounds, and ounces when the user pushes the Convert button."""

from tkinter import *

def convert_kg():
    #Convert value entered in the Entry area to grams, ounces & pounds
    grams = float(kg_entry_value.get()) * 1000
    pounds = float(kg_entry_value.get()) * 2.20462
    ounces = float(kg_entry_value.get()) * 35.274

    #Empty the text boxes if they had previous values and print the values converted in the text boxes
    gr_text.delete("1.0", END)#Empties the text box from start to end
    gr_text.insert(END, grams)
    pd_text.delete("1.0",END)
    pd_text.insert(END, pounds)
    on_text.delete("1.0", END)
    on_text.insert(END, ounces)

    #The delete method calls were added after checking the solution on Udemy

#Better yet, create a new button and function to clear the text boxes
def clear_text_boxes():
    gr_text.delete("1.0", END)
    pd_text.delete("1.0",END)
    on_text.delete("1.0", END)
    kg_entry.delete(0, END)
    

#Create main window 
main_window = Tk()
main_window.title("Weight converter")

#Create button widget and display it
cv_button = Button(main_window, text = "Convert", command = convert_kg)
cv_button.grid(row = 1, column = 3)

clear_button = Button(main_window, text = "Clear", command = clear_text_boxes)
clear_button.grid(row = 1, column = 4)

#Create a label widget and display it
kg_label = Label(main_window, text = "Kg")
kg_label.grid( row = 0, column = 2)

gr_label = Label(main_window, text = "Grams")
gr_label.grid( row = 2, column = 1)

pd_label = Label(main_window, text = "Pounds")
pd_label.grid( row = 2, column = 2)

on_label = Label(main_window, text = "Ounces")
on_label.grid( row = 2, column = 3)

#Create an entry widget and a StringVar variable for getting the value entered
kg_entry_value = StringVar()
kg_entry = Entry(main_window, textvariable = kg_entry_value)
kg_entry.grid(row =1, column = 2)

#Create text widget and display them
gr_text = Text(main_window, height = 1, width = 20)
gr_text.grid(row = 3, column = 1)
pd_text = Text(main_window, height = 1, width = 20)
pd_text.grid(row = 3, column = 2)
on_text = Text(main_window, height = 1, width = 20)
on_text.grid(row = 3, column = 3)



main_window.mainloop()