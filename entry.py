from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your Name: ", command=myClick)
myButton.pack()


root.mainloop()
