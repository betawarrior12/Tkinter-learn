from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code with Betawarrior12")
root.iconbitmap("C:\\Users\\USER\\Pemi\\PYTHON\\Tkinter-learn\\Images\\Tanjiro.ico")

def open():
    global myimg
    top = Toplevel()
    top.title("Coding Test")
    top.iconbitmap("C:\\Users\\USER\\Pemi\\PYTHON\\Tkinter-learn\\Images\\Naruto3.ico")
    myimg = ImageTk.PhotoImage(Image.open("Images\\Tanjiro.jpg"))
    myLabel = Label(top, image=myimg).pack()
    btn2 = Button(top, text="Close window", command=top.destroy).pack()


btn = Button(root, text="Open second Window", command=open).pack()

root.mainloop()
