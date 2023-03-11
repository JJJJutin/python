'''
當使用者輸入數值時，程式不僅提示再大再小還需要提示縮小過後的輸入範圍
EX:
請輸入0~100的整數:50
再小一點
請輸入0~50的整數:25
再小一點
請輸入0~25的整數:15
再大一點
請輸入15~25的整數:30
再小一點
請輸入15~25的整數:10
再大一點
請輸入15~25的整數:20
再大一點
請輸入20~25的整數:23
再大一點
請輸入23~25的整數:24
恭喜猜中!
'''
import random as r
import time as t
a = 100
b = 1
ans = (r.randint(1,100))
while True:
    x = int(input(f"請輸入{b}~{a}的整數:"))
    if x == ans:
        print("恭喜答對了")
        break
    elif x > ans:
        print("在小一點")
        if int(x) < int(a):
            a = x
    elif x < ans:
        print("在大一點")
        if int(x) > int(b):
            b = x
