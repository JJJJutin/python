import requests
from ttkbootstrap import *
from tkinter import filedialog, Label
import sys
import os
from PIL import Image, ImageTk

os.chdir(sys.path[0])

def on_switch_change():
    global temp
    if check_type == True:
        label3.config(text= f'溫度:{(int(temp)-32)*5/9}°C')
    else:
        label3.config(text= f'溫度:{int(temp)*9/5+32}°F')

def ans_show():
    api_key = "0ded44d7b7e6e734e1c0049be0cd8d2d"  #api key
    #api URL
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    try:
        city_name = entry.get()
    except:
        pass
    units = "metric" #單位(公制)
    lang = "zh_tw" #語言(繁體中文)

    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    print(send_url)

    response = requests.get(send_url)

    info = response.json()
    print(info)

    City = info["name"]
    label3.config(text= f'溫度:{info["main"]["temp"]}°C')
    label4.config(text= f'描述:{info["weather"][0]["description"]}')


    print(f'City = {City}')
    if "main" in info.keys():
        global temp
        icon_code = info["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f"{icon_code}.png", "wb") as icon_file:
            icon_file.write(response.content)

        image = Image.open(f"{icon_code}.png")
        tk_image = ImageTk.PhotoImage(image)
        label2.config(image=tk_image)
        label2.image = tk_image
        temp=info["main"]["temp"]
    else:
        print("city not found")
win = tk.Tk()











label = Label(win, text="請輸入想搜尋的城市:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(win, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

btn = Button(win, text="獲得天氣資訊", style="TButton", command=ans_show)
btn.grid(row=0, column=2, padx=10, pady=10)

label2 = Label(win, text="天氣圖標")
label2.grid(row=1, column=0, padx=10, pady=10)

label3 = Label(win, text="溫度:?°C")
label3.grid(row=1, column=1, padx=10, pady=10)

label4 = Label(win, text="描述:?")
label4.grid(row=1, column=2, padx=10, pady=10)

check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(win,variable=check_type,onvalue=True,offvalue=False,command=on_switch_change,text="溫度單位(°C/°F)")
check.grid(row=2, column=1)

win.mainloop()