from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code with Betawarior12 :)")
root.iconbitmap("C:\\Users\\USER\\Pemi\\PYTHON\\Tkinter-learn\\Naruto.ico")

myimg = ImageTk.PhotoImage(Image.open("Images\\betawarrior_edited.jpg"))
myLabel = Label(image=myimg)
myLabel.pack()


button_quit = Button(root, text="Exit Program", command=root.quit, fg="green")
button_quit.pack()

root.mainloop()
