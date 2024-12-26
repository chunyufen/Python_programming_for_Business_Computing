# week 2/PythonNewStyleColor.py

import turtle    # 导入turtle模块
def drawSnake(rad,angle,len,neckrad):   # 绘制一条蛇
    colors = ['red','yellow','blue','green','orange', 'magenta', 'gray', 'brown']   # 定义颜色列表
    for i in range(len):    # 循环len次
        turtle.color(colors[i])
        turtle.circle(rad,angle-i*2)   # 画圆
        turtle.circle(-rad,angle+i*2)   # 画圆
    turtle.color('red')
    turtle.circle(rad*3/2,angle/2)
    turtle.pensize(neckrad*5/2)
    turtle.fd(rad/2)

def init():
    turtle.setup(1000,1000,0,0)
    turtle.penup()
    turtle.goto(0,200)
    turtle.pendown()
    turtle.pensize(20)
    turtle.pensize(pythonsize)
    turtle.seth(-30)
    drawSnake(40,60,11,pythonsize/2)
    turtle.exitonclick()
    
init()    
