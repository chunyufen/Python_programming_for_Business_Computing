# week 2/MulticolorSpiral.py

"""This script uses the turtle graphics module to draw a multicolored spiral. The `draw_spin` function initializes the turtle's background color to black and then iterates 300 times, changing the pen color from a predefined list of colors, increasing the pen width, moving forward, and turning right at each step to create the spiral effect.
"""

import turtle  # 首先，代码导入了turtle模块，这是一个用于绘制图形的Python标准库。turtle模块提供了一个简单的绘图界面，可以通过编程控制一个虚拟的“海龟”在屏幕上移动并绘制图形。
t = turtle.Pen()  # 接下来，创建了一个turtle.Pen()对象，这个对象代表了绘图的海龟。通过这个对象，我们可以控制海龟的移动和绘图属性。
def draw_spin():  # 定义了一个名为draw_spin的函数，这个函数负责绘制螺旋线。在函数内部，首先定义了一个颜色列表colors，包含了六种颜色：橙色、蓝色、黄色、红色、紫色和绿色。
	colors = ['orange','blue','yellow','red','purple','green']
	turtle.bgcolor('black')  # 使用turtle.bgcolor('black')设置了绘图背景颜色为黑色。
	for x in range(300):  # 然后，代码进入一个循环，循环变量x从0到299。在每次循环中，执行以下操作
		turtle.pencolor (colors[x % 6])  # turtle.pencolor(colors[x % 6])：这行代码设置了海龟笔的颜色。x % 6的结果是x除以6的余数，这个余数用于从颜色列表中选择颜色，实现颜色的循环变化。
		turtle.width(x/100 + 1)  # turtle.width(x/100 + 1)：这行代码设置了海龟笔的宽度。随着x的增加，笔宽也会逐渐增加，x/100 + 1确保了笔宽至少为1，并且随着x的增加而增加。
		turtle.forward (x)  # turtle.forward(x)：这行代码让海龟向前移动x个单位长度，随着循环的进行，移动的距离会越来越长。
		turtle.right(59)  # turtle.right(59)：这行代码让海龟向右转动59度。这个角度的选择是为了让绘制的图形呈现出螺旋状。	
draw_spin()  # 最后，调用draw_spin()函数，开始绘制彩色螺旋线。







