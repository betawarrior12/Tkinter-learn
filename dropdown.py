from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code with Betawarrior12")
root.geometry("400x400")
root.iconbitmap("Images/Naruto2.ico")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Monday"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()
