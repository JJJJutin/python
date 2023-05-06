import matplotlib.pyplot as plt
import requests
from ttkbootstrap import *
from tkinter import filedialog, Label
import sys
import os
import datetime
from PIL import Image, ImageTk
from matplotlib.font_manager import FontProperties

os.chdir(sys.path[0])
font = FontProperties(fname= 'NotoSansTC-Medium.otf', size=14)



api_key = "892da2f13edf3c7f382637760e72d224"  #api key
#api URL
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
lon = "121.5319"
lat = "25.0478"
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

listX = []
listY = []
if "daily" in info.keys():
    for i in range(7):
        temp = info["daily"][i]["temp"]["day"]
        time = datetime.datetime.fromtimestamp(info["daily"][i]["dt"]).strftime("%m/%d")
        print(f"{time}的溫度是{temp}度")
        listX.append(time)
        listY.append(temp)
else:
    print("Request Fail")


fig, ax = plt.subplots() #創建圖表和軸
ax.plot(listX, listY) # 使用軸對象繪製圖表
ax.set_xlabel("日期", fontproperties=font) #設置x軸標籤
ax.set_ylabel("溫度", fontproperties=font) #設置y軸標籤
ax.set_title("這七天氣溫預測", fontproperties=font)

plt.show()