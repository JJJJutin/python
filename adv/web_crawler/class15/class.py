#######################匯入模組########################
from moviepy.editor import *
import sys
import os
from my_fun.my_fun import *
#######################初始化########################
os.chdir(sys.path[0])
#######################取得影片資訊########################
# url = "https://www.youtube.com/watch?v=eq8r1ZTma08"
url = input("輸入影片網址,n為跳過")
if url != "n":
    title, author, length, thumbnail_url, res = get_video_info(url)
    print(f"影片解析度:{res}")

#######################下載影片########################
r = input("根據上面資訊, 請輸入要下載的影片解析度(720p/480p/360p/240p/144p/n為跳過)")
if r != "n":
    if download_video(url, r):
        print("Download finished...")
    else:
        print("Download failed...")
#######################切割影片########################
r = input("要不要切割影片(y/n)")
if r != "n":
    beg = int(input("請輸入要切割的開始時間(秒):"))
    end = int(input("請輸入要切割的結束時間(秒):"))
    result = "剪輯完成" if cut_video(f"{title}.mp4", beg, end) else "剪輯失敗"
    print(result)
#######################合併影片########################
r = input("要不要合併影片(y/n)")
if r != "n":
    file_name_list = []
    for i in range(15):
        file_name_list.append("命に嫌われている。／まふまふ【歌ってみた】-0-5.mp4")
    # file_name_list = ["【小小兵】第三支精采可愛預告-9-10.mp4", "【小小兵】第三支精采可愛預告-9-10.mp4", "【小小兵】第三支精采可愛預告-9-10.mp4"]
    # if merge_video(file_name_list, "合併影片.mp4"):
    #     print("合併影片成功")
    # else:
    #     print("合併影片失敗")
    result = "合併影片成功" if merge_video(file_name_list, "合併影片.mp4") else "合併影片失敗"
    print(result)

#######################影片轉GIF########################
r = input("要不要影片轉GIF(y/n)")
if r != "n":
    video_path = "合併影片.mp4"
    gif_path = "命に嫌われている。／まふまふ【歌ってみた】-0-5.gif"

    result = "影片轉GIF成功" if video_to_gif(video_path, gif_path) else "影片轉GIF失敗"
    print(result)