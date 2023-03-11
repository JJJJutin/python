import turtle as t
# turtle.color("blue") #設定烏龜顏色
# turtle.shape("circle") #設定烏龜形"arrow", "turtle", "circle", "square", "triangle", "classic"
# turtle.stamp() #蓋章
# turtle.penup() #提筆
# turtle.pendown() #下筆
t.fillcolor("green")
t.begin_fill()

t.color("green")
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)

t.forward(25)
t.left(90)
t.penup()
t.forward(25)
t.right(150)
t.pendown()

t.penup()
t.forward(30)
t.pendown()
t.forward(30)
t.right(120)
t.forward(60)
t.right(120)
t.forward(30)
t.penup()
t.forward(30)
t.pendown()

t.right(150)
t.penup()
t.forward(30)
t.pendown()

t.left(30)
t.forward(70)
t.right(120)
t.forward(70)
t.right(120)
t.forward(70)

t.end_fill()

t.backward(70)
t.right(60)
t.forward(35)
t.right(90)

t.pencolor("brown")
t.pensize(20)
t.forward(25)



t.done() #保持顯示