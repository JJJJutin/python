"""
輸入三角形三邊(存入變數a, b, c中) 
判斷是否能構成三角形(利用邊長運算進行判斷，可以上網搜尋公式)
是三角形:則顯示面積和周長
不是:則顯示，
"""
print("輸入三角形三邊")
a = float(input("輸入邊a:"))
b = float(input("輸入邊b:"))
c = float(input("輸入邊c:"))
if a + b > c:
    all = a + b + c
    p = 1/2 (a+b+c)
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
else:
    print("無法構成三角形")
