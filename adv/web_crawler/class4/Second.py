from ttkbootstrap import *
from tkinter import filedialog, Label
import sys
import os
from PIL import Image, ImageTk

def ans_show():
    try:
        
        label.config(text=eval(entry.get()), fg = "white")
    except:
        label.config(text="ERROR", fg="red")

font_size = 10

win = tk.Tk()
win.title("Nyan_Cat")
win.option_add("*font", ("Helvetica", font_size))


style = Style(theme="solar")
style.configure("TButton", font=("Helvetica", font_size))

entry = Entry(win, width=30)

entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10) #padx, pady為元件與元件之間的距離

btn = Button(win, text="顯示計算結果", style="TBUtton", command=ans_show)
btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10) #W=West

label = Label(win, text="計算結果")
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)



win.mainloop()