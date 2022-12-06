from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Code with Betawarrior12")
root.iconbitmap("Images/Tanjiro6.ico")

def open():
    global myimg 
    root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\USER\\Pemi\\PYTHON\\Tkinter-learn\\Images", title="Select A file...", filetypes=(("jpeg files", "*.jpg"), ("All files", "*.*")))
    myLabel = Label(root, text=root.filename).pack()

    myimg = ImageTk.PhotoImage(Image.open(root.filename))
    myimg_label = Label(image=myimg).pack()

myButton = Button(root, text="Open file", command=open).pack()

root.mainloop()
