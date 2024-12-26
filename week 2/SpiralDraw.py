# week 2/SpiralDraw.py

"""我们首先导入了turtle模块。然后定义了一个名为draw_spiral()的函数，用于绘制螺旋中的螺旋。

在draw_spiral()函数中，我们设置了绘制速度为10，初始线段长度为1，初始旋转角度为90。然后使用循环绘制100个线段，每次向前绘制线段，然后右转指定角度，同时增加线段长度和减小旋转角度。最后调用turtle.done()函数完成绘制。
"""

import turtle

def draw_spiral():
    turtle.speed(10)  # 设置绘制速度
    length = 1  # 设置初始线段长度
    angle = 90  # 设置初始旋转角度

    for _ in range(100):  # 绘制100个线段
        turtle.forward(length)  # 向前绘制线段
        turtle.right(angle)  # 右转指定角度
        length += 2  # 增加线段长度
        angle -= 0.5  # 减小旋转角度

    turtle.done()  # 完成绘制

draw_spiral()