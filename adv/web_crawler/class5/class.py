import requests
from ttkbootstrap import *
from tkinter import filedialog, Label
import sys
import os
from PIL import Image, ImageTk

def on_switch_change():
    print("text")


win = tk.Tk()

api_key = "0ded44d7b7e6e734e1c0049be0cd8d2d"  #api key
#api URL
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name:")
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
Temperature = info["main"]["temp"]
Description = info["weather"][0]["description"]


print(f'City = {City}')
print(f'Temperature = {Temperature}')
print(f'Description = {Description}')

os.chdir(sys.path[0])

if "main" in info.keys():
    icon_code = info["weather"][0]["icon"]
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f"{icon_code}.png", "wb") as icon_file:
        icon_file.write(response.content)
else:
    print("city not found")

check_type = BooleanVar()
check_type.set(True)

check_label = Label(win, text="True")
check_label.grid(row=1, column=2)

check = Checkbutton(win,
                      variable=check_type,
                      onvalue=True,
                      offvalue=False,
                      command=on_switch_change)
check.grid(row=1, collumn=1)
win.mainloop()