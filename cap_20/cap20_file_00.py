"""Building a GUI with Tkinter"""

#Importing all from tkinter
from tkinter import *

#A tkinter GUI is build from two parts: window and wdigets
#Create a window
window = Tk()

#Create a button widget
b1 = Button(window, text = "Press me")

#b1.pack() #This will show the widget in the window
b1.grid(row = 1, column = 3) #Will do the same as b1.pack() but this method has more control over the widget, such as position of widget

#Add an entry widget
e1 = Entry(window)
e1.grid(row = 1, column = 4) #An entry is an area where the user can enter data

#Add a text widget
t1 = Text(window, height = 1, width = 20) #Default values for text widget will create a large window for text, that is way we need to edit the height and width according to our needs. You can also check the default values by passing only the window parameter 
t1.grid(row = 1, column = 5)


window.mainloop()