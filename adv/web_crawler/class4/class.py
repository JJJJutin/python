from ttkbootstrap import *
from tkinter import filedialog
import sys
import os
from PIL import Image, ImageTk
os.chdir(sys.path[0]) #設定工作目錄
def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0]) #initialdir=sys.path[0] 預設打開位置
    lable2.config(text=file_path) #顯示名稱

def show_image():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo # type: ignore # 保留照片, 避免被回收

def test():
    print("test")

def quit_fun():
    win.destroy()

def Nyan():
    print("Nyan")

font_size = 20

win = tk.Tk()
win.title("Nyan_Cat")
win.option_add("*font", ("Helvetica", font_size))

style = Style(theme="solar")
style.configure("TButton", font=("Helvetica", font_size))

lable = Label(win, text="Nyan")
lable.grid(row=0, column=0, sticky="E")

lable2 = Label(win, text="N")
lable2.grid(row=0, column=1, rowspan=1, sticky="E")

btn = Button(win, text="Cat")
btn.grid(row=0, column=2, sticky="W") #W=West

btn2 = Button(win, text="Quit", command=quit_fun, style="TButton")
btn2.grid(row=1, column=0, columnspan=3, sticky="EW")

canvas = Canvas(win, width=800, height=600, bg="black")
canvas.grid(row=2, column=0, columnspan=3)

win.mainloop()