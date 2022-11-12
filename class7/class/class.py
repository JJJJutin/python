# for i in range(2, 6):
#     print(i)
# else:
#     print("迴圈正常結束")

# i = 2
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("迴圈正常結束")

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# while True:
#     print("1.蘋果汁")
#     print("2.柳橙汁")
#     print("3.葡萄汁")
#     print("4.系統關閉")  
# try:
#     x = int(input("請輸入編號:"))
# except:
#     print("分不清數字和文字喔")
# if x == 4 :
#     print("系統已關閉")
#     break
# elif x == 3 :
#     print("您點的飲料是葡萄汁")
# elif x == 2 :
#     print("您點的飲料是柳橙汁")
# elif x == 1 :
#     print("您點的飲料是蘋果汁")
# else:
#     print("看不懂數字嗎?沒上過幼稚園嗎?")

# while True:
#     print(r.randrange(10))
import random as r
import time as t

ans = (r.randint(1,100))
while True:
    x = int(input("請輸入1~100的整數:"))
    if x == ans:
        print("恭喜答對了")
        break
    elif x > ans:
        print("在小一點")
    elif x < ans:
        print("在大一點")