from pytube import YouTube  # pip install -U pytube
import os
import sys
import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def call_weather_api(lon: str = "121.5319", lat: str = "25.0478") -> dict:
    """ 使用OpenWeatherMap API獲取天氣資訊 """
    # 使用OpenWeatherMap API獲取天氣資訊
    api_key = "892da2f13edf3c7f382637760e72d224"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    exclude = "minutely,hourly"  # 不要分鐘級和小時級的資料
    units = "metric"
    lang = "zh_tw"

    send_url = base_url
    send_url += "lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    response = requests.get(send_url)  # 發送請求，獲得天氣資訊
    info = response.json()  # 將json格式轉換為字典
    return info


def get_plot_fig(xlist, ylist, title, xlabel, ylabel) -> plt.Figure:
    """建立圖表"""
    # 建立圖表
    module_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(module_dir, 'NotoSansTC-Medium.otf')
    font = FontProperties(fname=font_path, size=14)
    fig, ax = plt.subplots()  # 建立圖表
    ax.plot(xlist, ylist)
    ax.set_title(title, fontproperties=font)
    ax.set_ylabel(ylabel, fontproperties=font)
    ax.set_xlabel(xlabel, fontproperties=font)
    return fig

    # ax.plot(dates, temps)
    # ax.set_title("7天氣溫預測", fontproperties=font)
    # ax.set_ylabel("溫度 (°C)", fontproperties=font)
    # ax.set_xlabel("日期", fontproperties=font)


def save_weather_icon(icon_code):
    """下載並保存天氣圖標"""
    # 下載並保存天氣圖標
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f"{icon_code}.png", "wb") as icon_file:
        icon_file.write(response.content)


def get_7_Days_weather(info: dict):
    """獲取七天天氣資訊, 回傳日期和溫度的list"""
    # 獲取七天天氣資訊, 建立日期和溫度的list
    dates = []
    temps = []
    for i in range(7):
        temp = info["daily"][i]["temp"]["day"]
        time = datetime.datetime.fromtimestamp(
            info["daily"][i]["dt"]).strftime("%m/%d")
        dates.append(time)
        temps.append(temp)
        print(f"{time} 的溫度是 {temp} 度")
    return dates, temps


def get_video_info(url: str):
    yt = YouTube(url)
    print(f"影片名稱:{yt.title}")  # 取得影片的標題資訊
    print(f"影片作者:{yt.author}")  # 取得影片的作者資訊
    print(f"影片長度:{yt.length}秒")  # 取得影片的長度資訊
    print(f"縮圖網址:{yt.thumbnail_url}")  # 取得影片的縮圖網址

    streams = yt.streams.filter(progressive=True, file_extension='mp4')

    res = []
    for stream in streams:
        res.append(stream.resolution)

    return yt.title, yt.author, yt.length, yt.thumbnail_url, res


def download_video(url: str, r: str):
    yt = YouTube(url)

    streams = yt.streams.filter(progressive=True, file_extension='mp4')

    res = []
    for stream in streams:
        res.append(stream.resolution)

    if r in res:
        stream = streams.filter(res=r)[0]
        stream.download()
        print("下載完成")
        return True
    else:
        print("找不到該解析度的影片")
        return False