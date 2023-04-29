import matplotlib.pyplot as plt

listX = [1, 2, 3, 4, 5, 6]
listY = [20, 30, 37, 21, 33, 40]

fig, ax = plt.subplots() #創建圖表和軸
ax.plot(listX, listY) # 使用軸對象繪製圖表
ax.set_xlabel("X Label") #設置x軸標籤
ax.set_ylabel("Y Label") #設置y軸標籤
ax.set_title("New Title")

plt.show()