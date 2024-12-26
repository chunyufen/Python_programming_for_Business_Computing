# week 2/PythonColorDraw.py

import turtle
import random  # 导入随机数模块实现随机颜色的功能
# 把不同颜色用字典的方式储存 key为1到6的整数
colors = {1:'blue',2:'yellow',3:'red',4:'purple',5:'black',6:'green'}
turtle.setup(650,350,200,200)
turtle.pu()
turtle.fd(-250)
turtle.pendown()
turtle.width(25)
turtle.seth(-40)
for i in range(4):
    a = random.randrange(1,7)  # 获取随机数并赋值给a
    turtle.pencolor(colors[a])  # 通过索引的方式选择颜色（颜色是随机的）
    turtle.circle(40,80)
    a = random.randrange(1,7)  # 获取随机数并赋值给a
    turtle.pencolor(colors[a])  # 通过索引的方式选择颜色（颜色是随机的）
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
