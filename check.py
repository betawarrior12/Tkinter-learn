from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code with Betawarrior12")
root.geometry("400x400")
root.iconbitmap("Images/Tanjiro4.ico")

def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Would you like to Supersize your order? Click here.", variable=var, onvalue="Supersize", offvalue="Regularsize")
c.deselect()
c.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()
