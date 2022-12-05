from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look I clicked a button")
    myLabel.pack()


myButton = Button(root, text="Click Me ! :)", command=myClick, fg="blue")
myButton.pack()


root.mainloop()
