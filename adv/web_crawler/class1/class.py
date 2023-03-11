from tkinter import *
import random as r

color = [
    "black",
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "lime",
    "maroon",
    "navy",
    "olive",
    "teal",
    "violet",
    "indigo",
    "coral",
    "crimson",
    "hotpink",
    "khaki",
    "lavender",
    "lavenderblush",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightsteelblue",
    "lightyellow",
]

def hi_fun():
    global change
    if change == False:
        lable.config( text="Hi", fg=color[r.randrange(0, len(color))], bg=color[r.randrange(0, len(color))])
    else:
        lable.config( text="Hi", fg=r.choice(color), bg=r.choice(color))
    change = not (change)

change = False

win = Tk()
win.title("my first GUI")

btn = Button(win, text="Hello", command=hi_fun)
btn.pack()

lable = Label(win, text="Hi", fg="black")
lable.pack()

win.mainloop()
"""
# import modules
from tkinter import *
import os


# user define function
def shutdown():
	return os.system("shutdown /s /t 1")

def restart():
	return os.system("shutdown /r /t 1")

def logout():
	return os.system("shutdown -l")


# tkinter object
master = Tk()

# background set to grey
master.configure(bg='light grey')

# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="Shutdown", command=shutdown).grid(row=0)
Button(master, text="Restart", command=restart).grid(row=1)
Button(master, text="Log out", command=logout).grid(row=2)

mainloop()
"""