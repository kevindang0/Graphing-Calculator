from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk

root = CTk()
root.geometry("800x600")


mainmenu = Image.open("../pics/mainmenu.png")
mainmenu = mainmenu.resize((1000, 750))
mainmenu = ImageTk.PhotoImage(mainmenu)

img = Label(root, image=mainmenu)
img.place(x=0, y=0, relwidth=1, relheight=1)
img.pack()

root.mainloop()

