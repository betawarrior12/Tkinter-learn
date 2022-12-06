from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code with Betawarrior12")
root.iconbitmap("Images/Tanjiro2.ico")
root.geometry("400x400")


def slide():
    myLabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

myLabel = Label(root, text=horizontal.get()).pack()

myButton = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
