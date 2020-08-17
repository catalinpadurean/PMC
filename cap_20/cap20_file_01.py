"""Building a GUI with Tkinter"""

from tkinter import *

def km_to_miles():
    miles = float(e1_value.get()) * 1.6 #e1_value.get() method will retrieve the value entered in the entry area
    t1.insert(END, miles) #Will insert the second argument in the textbox at the location specified by the first argument

window = Tk()
#Create a button and add an action for the button
b1 = Button(window, text = "Execute", command = km_to_miles) #The function passed as an "command argument" will be executed when the button is pressed
b1.grid(row = 1, column = 3)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value) #textvariable argument expects an StrinVar type.
e1.grid(row = 1, column = 4)

t1 = Text(window, height = 1, width = 20) #Default values for text widget will create a large window for text, that is way we need to edit the height and width according to our needs. You can also check the default values by passing only the window parameter 
t1.grid(row = 1, column = 5)

window.mainloop()