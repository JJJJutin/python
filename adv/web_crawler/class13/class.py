#######################匯入模組########################
from ttkbootstrap import *
import time


#######################指令########################
def start_progress():
    for i in range(101):
        progress["value"] = i
        percent_label.config(text=f"{i}%")
        window.update()


#######################建立視窗########################
window = tk.Tk()
window.title("Progress Bar Example")

#######################建立元件########################
#進度條
progress = Progressbar(window,
                       orient=HORIZONTAL,
                       length=200,
                       mode='determinate')
progress.grid(row=0, column=0, padx=10, pady=10)
#進度條百分比標籤
percent_label = Label(window, text="")
percent_label.grid(row=0, column=1, padx=10, pady=10)
#開始按鈕
start_button = Button(window, text="Start", command=start_progress)
start_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
#######################運行應用程式########################
window.mainloop()