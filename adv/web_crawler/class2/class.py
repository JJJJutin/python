from tkinter import *
import sys as s
import os as o

i = 0

o.chdir(s.path[0]) #設定工作目錄

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

# def move_canvas(event):
#     key = event.keysym
#     print(key)
#     if key == "Right":
#         canvas.move(Nyan_cat, 10, 0)
#     elif key == "Left":
#         canvas.move(Nyan_cat, -10, 0)
#     elif key == "Up":
#         canvas.move(Nyan_cat, 0, -10)
#     elif key == "Down":
#         canvas.move(Nyan_cat, 0, 10)

# 定義移動物件的函式，接受一個事件、物件、水平位移和垂直位移
# event: 事件物件為canvas.bind_all要求傳入的參數
def move_object(event, object, dx, dy):
    canvas.move(object, dx, dy)

def quit_fun():
    win.destroy()

win = Tk()
win.title("Nyan_Cat")

canvas = Canvas(win, width=800, height=600, bg="black")
canvas.pack()

img = PhotoImage(file="Nyan_cat.png") #載入圖片

circle = canvas.create_oval(100, 50, 550, 500, outline="white")

Nyan_cat = canvas.create_image(400, 300, image=img)

msg = canvas.create_text(400, 20, text="Space", fill="white", font=("Arial", 30))

# canvas.bind_all("<Key>", move_canvas)
# 將按鍵事件綁定到畫布上，當按下指定的按鍵時，移動對應的物件
canvas.bind_all('<Right>', lambda event: move_object(event, circle, 5, 0))
canvas.bind_all('<Left>', lambda event: move_object(event, circle, -5, 0))
canvas.bind_all('<Up>', lambda event: move_object(event, circle, 0, -5))
canvas.bind_all('<Down>', lambda event: move_object(event, circle, 0, 5))
canvas.bind_all('<d>', lambda event: move_object(event, Nyan_cat, 10, 0))
canvas.bind_all('<a>', lambda event: move_object(event, Nyan_cat, -10, 0))
canvas.bind_all('<w>', lambda event: move_object(event, Nyan_cat, 0, -10))
canvas.bind_all('<s>', lambda event: move_object(event, Nyan_cat, 0, 10))

quit = Button(win, text="Quit", command=quit_fun)
quit.pack()

mainloop()