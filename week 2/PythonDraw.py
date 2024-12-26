# week 2/PythonDraw.py

"""This script uses the turtle graphics module to draw a complex geometric pattern. It sets up the screen, moves the turtle to a specific starting point, and then executes a series of circle and forward movements to create a unique design. The pattern consists of alternating circles with different radii and orientations, followed by a final sequence that includes a smaller circle and a line segment. This code is an implementation detail of a graphical representation within the Python Foundation course materials.
"""
import turtle
turtle.setup(650,350,200,200)  # 首先，代码通过turtle.setup(650,350,200,200)设置了绘图窗口的大小和位置，其中650和350分别是窗口的宽度和高度，而200,200是窗口左上角相对于屏幕的位置。
turtle.penup()  # 接着，turtle.penup()命令使乌龟抬起笔，这样它在移动时不会绘制线条。然后，turtle.fd(-250)命令让乌龟向前移动-250个单位，实际上是向后移动250个单位，这可能是为了将乌龟移动到绘图的起始位置。
turtle.fd(-250)
turtle.pendown()  # 之后，turtle.pendown()命令放下笔，准备开始绘制。turtle.pensize(25)设置了笔的粗细为25个单位，turtle.pencolor("purple")设置了笔的颜色为紫色。
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)  # turtle.seth(-40)命令设置了乌龟的初始方向为-40度（逆时针方向）。接下来的for循环执行了四次，每次循环中，乌龟先顺时针画一个半径为40，角度为80度的圆弧，然后逆时针画一个半径为40，角度为80度的圆弧。这四个圆弧组成了一个类似花瓣的图形。
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)  # 循环结束后，turtle.circle(40,80/2)命令让乌龟画了一个半径为40，角度为40度的圆弧，这是花瓣图形的一部分。turtle.fd(40)命令让乌龟向前移动40个单位。
turtle.fd(40)
turtle.circle(16,180)  # 紧接着，turtle.circle(16,180)命令绘制了一个半径为16，角度为180度的半圆，这可能是花瓣图形的一部分或者是另一个独立的图形元素。
turtlefd(40*2/3)  # 最后，turtlefd(40*2/3)这行代码有一个小错误，应该是turtle.fd(40*2/3)，它让乌龟向前移动了80/3个单位。turtle.done()命令结束绘图并保持窗口打开。
turtle.done()