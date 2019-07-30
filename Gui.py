from tkinter import *
from tkinter import filedialog
import tkinter.messagebox

def printInfo():
    tkinter.messagebox.showinfo("About","This program is developed by Darshan!!")

def browsePic():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

root = Tk()
root.configure(bg="AntiqueWhite1")

topframe = Frame(root)
topframe.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topframe, text="Upload", fg="red", bg="black",command=browsePic).pack()
button2 = Button(topframe, text="About", fg="red", bg="black",command=printInfo).pack()
button3 = Button(bottomFrame, text="Exit", fg="red", bg="black",command=root.destroy).pack()

pathlabel = Label(root)
pathlabel.pack()

root.mainloop()
