

from PIL import Image, ImageTk
from ttkbootstrap import *
import sys as s
import os as o

o.chdir(s.path[0])

# def move_object(event, object, dx, dy):
#     canvas.move(object, dx, dy)

# def test():
#     print("test")

def quit_fun():
    win.destroy()

def Nyan():
    print("Nyan")

font_size = 20 #共同字型大小

win = tk.Tk()
win.title("Nyan_Cat")
win.option_add("*font", ("Helvetica", font_size)) #設定預設字型

style = Style(theme="solar")
style.configure("TButton", font=("Helvetica", font_size)) #設定按鈕字型



lable = Label(win, text="Nyan")
lable.grid(row=0, column=0, sticky="E") #sticky=E 靠右對齊 E=East

lable2 = Label(win, text="N")
lable2.grid(row=0, column=1, rowspan=1, sticky="E") #sticky=E 靠右對齊 E=East


btn = Button(win, text="Cat")
btn.grid(row=0, column=2, sticky="W") #W=West

btn2 = Button(win, text="Quit", command=quit_fun, style="TButton")
btn2.grid(row=1, column=0, columnspan=3, sticky="EW")

canvas = Canvas(win, width=800, height=600, bg="black")
canvas.grid(row=2, column=0, columnspan=3)
"""
image = Image.open("cat-nyan-cat.gif")
img = ImageTk.PhotoImage(image)

Nyan_cat = canvas.create_image(400, 300, image=img)

canvas.bind_all('<d>', lambda event: move_object(event, Nyan_cat, 10, 0))
canvas.bind_all('<a>', lambda event: move_object(event, Nyan_cat, -10, 0))
canvas.bind_all('<w>', lambda event: move_object(event, Nyan_cat, 0, -10))
canvas.bind_all('<s>', lambda event: move_object(event, Nyan_cat, 0, 10))
"""
win.mainloop()