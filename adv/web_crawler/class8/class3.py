import requests
from ttkbootstrap import *
from tkinter import filedialog, Label
import sys
import os
import datetime
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.font_manager import FontProperties

os.chdir(sys.path[0])

listX = []
listY = []
font = FontProperties(fname= 'NotoSansTC-Medium.otf', size=14)

def on_switch_change():
    global temp0, units
    print("kkk")
    if check_type.get():
        units = "metric" 
        print("m")
    else:
        units = "imperial" 
        print("i")

    if label3.cget("text") != "溫度:?°C":
        if units == "metric":
            temp0 = round((temp0 - 32) * 5 / 9, 2)
            label3.config(text= f'溫度:{temp0}°C')
        elif units == "imperial":
            temp0 = round((temp0 * 9 / 5) + 32, 2)
            label3.config(text= f'溫度:{temp0}°F')

def ans_show():
    global units, info, temp, temp0
    api_key = "892da2f13edf3c7f382637760e72d224"  #api key
    #api URL
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    if entry.get() == "":
        lon = "121.5319"
    else:
        lon = entry.get()
    if entry2.get() == "":
        lat = "25.0478"
    else:
        lat = entry.get()
    exclude = "minutely,hourly"
    units = "metric" #單位(公制)
    lang = "zh_tw" #語言(繁體中文)

    send_url = base_url
    send_url += "appid=" + api_key
    send_url += "&lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    print(send_url)

    response = requests.get(send_url)
    info = response.json()

    
        # api_key = "0ded44d7b7e6e734e1c0049be0cd8d2d"  #api key
    # #api URL
    # base_url = "https://api.openweathermap.org/data/2.5/weather?"
    # try:
    #     city_name = entry.get()
    # except:
    #     pass
    units = "metric" #單位(公制)
    # lang = "zh_tw" #語言(繁體中文)

    # send_url = base_url
    # send_url += "appid=" + api_key
    # send_url += "&q=" + city_name
    # send_url += "&units=" + units
    # send_url += "&lang=" + lang
    # print(send_url)

    # response = requests.get(send_url)

    # info = response.json()
    # print(info)

    City = info["timezone"]
    label3.config(text= f'溫度:{info["current"]["temp"]}°C')
    label4.config(text= f'描述:{info["current"]["weather"][0]["description"]}')


    print(f'City = {City}')
    if "daily" in info.keys():
        for i in range(7):
            temp = info["daily"][i]["temp"]["day"]
            if i == 0:
                temp0 = temp
            time = datetime.datetime.fromtimestamp(info["daily"][i]["dt"]).strftime("%m/%d")
            print(f"{time}的溫度是{temp}度")
            listX.append(time)
            listY.append(temp)
            fig, ax = plt.subplots() #創建圖表和軸
            ax.plot(listX, listY)
            ax.plot(listX, listY, "o") # 使用軸對象繪製圖表
            ax.set_xlabel("日期", fontproperties=font) #設置x軸標籤
            ax.set_ylabel("溫度", fontproperties=font) #設置y軸標籤
            ax.set_title("這七天氣溫預測", fontproperties=font)
            canvas = FigureCanvasTkAgg(fig, master=win)

            canvas.draw()
            canvas = canvas.get_tk_widget()
            canvas.grid(row=0, column=0, padx=10, pady=10)
            canvas = FigureCanvasTkAgg(fig, master=win)
            canvas.draw()
            canvas = canvas.get_tk_widget()
            canvas.grid(row=0, column=0, padx=10, pady=10)
        else:
            print("city not found")
win = tk.Tk()






def on_closing():
    win.destroy()
    plt.close("all")



win.protocol("WM_DELETE_WINDOW", on_closing)
style = Style(theme="minty")






label = Label(win, text="請輸入想搜尋的城市:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(win, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)
entry2 = Entry(win, width=30)
entry2.grid(row=1, column=1, padx=10, pady=10)

btn = Button(win, text="獲得天氣資訊", style="TButton", command=ans_show)
btn.grid(row=0, column=2, padx=10, pady=10)

label2 = Label(win, text="天氣圖標")
label2.grid(row=2, column=0, padx=10, pady=10)

label3 = Label(win, text="溫度:?°C")
label3.grid(row=2, column=1, padx=10, pady=10)

label4 = Label(win, text="描述:?")
label4.grid(row=2, column=2, padx=10, pady=10)

check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(win,variable=check_type,onvalue=True,offvalue=False,command=on_switch_change,text="溫度單位(°C/°F)")
check.grid(row=3, column=1)

win.mainloop()