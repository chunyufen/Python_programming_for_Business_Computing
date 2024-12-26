# week 2/PythonColorDraw2.py

import turtle
import random  # 导入随机数模块实现随机颜色的功能
turtle.colormode(255)  # 把颜色表示法取值的模式从[0-1]之间改成[0-255]
#定义一个生成颜色的模块
def colorchoose():
    a, b, c = random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)
    color = (a, b, c)
    return color   #返回值是一个rgb颜色
turtle.setup(650, 350, 200, 200) 
turtle.pu()
turtle.fd(-250)
turtle.pendown()
turtle.width(25)
turtle.seth(-40)
for i in range(4):
    turtle.pencolor(colorchoose())  # 调用模块 随机生成rgb颜色
    turtle.circle(40, 80)
    turtle.pencolor(colorchoose())  # 调用模块 随机生成rgb颜色
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
 