# def hello(name):
#     print(f"hello {name}!")
# def WTF():
#     print(f"{x}!What The Heck!")
# x = (input("Enter Your Name:"))
# hello(x)
# WTF()
# def my_min(a, b):
#     if a < b:
#         return a
#     else:
#         return b
# y = my_min(1, 2)
# print("My Min:", y)
import random as r

def random_dice(n):
    d = {}
    
    for z in range(n):
        k = (f"第{z + 1}次")
        v = r.randint(1, 6)
        d[k] = v
    print(f"骰出的答案分別是{d}")
x = int(input("請輸入要骰骰子的次數:"))
random_dice(x)