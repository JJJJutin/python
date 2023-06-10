from ttkbootstrap import *
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from weather_fun import weather_fun as wf

os.chdir(sys.path[0])

######################主程式########################
u = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def get_video_info_gui():
    _, _, _, _, res = wf.get_video_info(entry.get())

    res_option["menu"].delete(0, "end")
    for r in res:
        res_option["menu"].add_command(label=r, command=tk._setit(res_var, r))

    res_var.set(res[0])


def download_video_gui():

    if wf.download_video(entry.get(), res_var.get(), show_progress):
        label3.config(text="下載完成")
    else:
        label3.config(text="下載失敗")


def show_progress(stream, chunk, bytes_remaining):
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize

    percent_label.config(text=f"{percent:.2f}%")

    progress["value"] = percent

    window.update()


######################版面########################
font_size = 10
window = tk.Tk()
window.title("YT Video Bot")
window.option_add("*font", ("Helvetica", font_size))

style = Style(theme="minty")
style.configure('my.TButton', font=('Helvetica', font_size))
style.configure('my.TCheckbutton', font=('Helvetica', font_size))

city_name_label = Label(window, text="請輸入Youtube影片網址:")
city_name_label.grid(row=0, column=0, padx=10, pady=10)

search_button = Button(window,
                       text="獲得影片資訊",
                       command=get_video_info_gui,
                       style='my.TButton')
search_button.grid(row=0, column=2, padx=10, pady=10)

var = tk.StringVar()
var.set(u)
entry = Entry(window, width=20, textvariable=var)
entry.grid(row=0, column=1, padx=10, pady=10)

label = Label(window, text="請選擇影片解析度")
label.grid(row=2, column=0, padx=10, pady=10)

res_var = tk.StringVar()
res_option = OptionMenu(window, res_var, ())
res_option.grid(row=2, column=1, padx=10, pady=10)

download_button = Button(window,
                         text="下載影片",
                         command=download_video_gui,
                         style='my.TButton')
download_button.grid(row=2, column=2, padx=10, pady=10)

label3 = Label(window, text="下載完成")
label3.grid(row=3, column=0, padx=10, pady=10)

#進度條
progress = Progressbar(window,
                       orient=HORIZONTAL,
                       length=200,
                       mode='determinate')
progress.grid(row=3, column=1, padx=10, pady=10)
#進度條百分比標籤
percent_label = Label(window, text="")
percent_label.grid(row=3, column=2, padx=10, pady=10)

window.mainloop()