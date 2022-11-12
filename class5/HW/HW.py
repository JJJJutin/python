"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""
import turtle
turtle.tracer(0, 0)
turtle.shape("circle")
turtle.stamp()
for start in range(0, 360, 45):
    turtle.home()
    turtle.right(start)
    turtle.penup()
    turtle.forward(100)
    turtle.stamp()
turtle.done()