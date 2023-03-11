import turtle

# turtle.forward(100) #int or float
# turtle.backward(100) #int or float
# turtle.left(90) #int or float
# turtle.right(90) #int or float

# for block in range(0, 8, 2):
#     turtle.forward(100)
#     turtle.right(90)

# turtle.color("blue") #設定烏龜顏色
# turtle.shape("circle") #設定烏龜形"arrow", "turtle", "circle", "square", "triangle", "classic"
# turtle.stamp() #蓋章
# turtle.penup() #提筆
# turtle.pendown() #下筆

# turtle.shape("circle")
# for circle in range(0, 1000, 3):
#     turtle.penup()
#     turtle.forward(circle)
#     turtle.right(35)
#     turtle.stamp()

# turtle.pensize(5) #線徑寬度1~10
# turtle.pencolor("yellow") #線的顏色
# turtle.fillcolor("yellow") #區域填滿顏色
# turtle.begin_fill() #填滿區域設定開始
# turtle.end_fill() #填滿區域設定結束

turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
for start in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill()
turtle.done() #保持顯示

