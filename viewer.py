from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Code with Betawarior12 :)")
root.iconbitmap("C:\\Users\\USER\\Pemi\\PYTHON\\Tkinter-learn\\Images\\Naruto.ico")

Images = []

myimg1 = ImageTk.PhotoImage(Image.open("Images\\betawarrior.jpg"))
Images.append(myimg1)

myimg2 = ImageTk.PhotoImage(Image.open("Images\\Naruto.jpg"))
Images.append(myimg2)

myimg3 = ImageTk.PhotoImage(Image.open("Images\\Naruto2.jpg"))
Images.append(myimg3)

myimg4 = ImageTk.PhotoImage(Image.open("Images\\Naruto3.jpg"))
Images.append(myimg4)

myimg5 = ImageTk.PhotoImage(Image.open("Images\\Naruto4.jpg"))
Images.append(myimg5)

myimg6 = ImageTk.PhotoImage(Image.open("Images\\Tanjiro.jpg"))
Images.append(myimg6)

myimg7 = ImageTk.PhotoImage(Image.open("Images\\Tanjiro2.jpg"))
Images.append(myimg7)

myimg8 = ImageTk.PhotoImage(Image.open("Images\\Tanjiro3.jpg"))
Images.append(myimg8)

myimg9 = ImageTk.PhotoImage(Image.open("Images\\Tanjiro4.jpg"))
Images.append(myimg9)

myimg10 = ImageTk.PhotoImage(Image.open("Images\\Tanjiro5.jpg"))
Images.append(myimg10)

myimg11 = ImageTk.PhotoImage(Image.open("Images\\Tanjiro6.jpg"))
Images.append(myimg11)


myLabel = Label(image=myimg1)
myLabel.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=Images[image_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number == len(Images):
        button_forward = Button(root, text=">>", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(image_number):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=Images[image_number - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
