# week 1/Circles.py
"""This script uses the turtle graphics module to draw a series of concentric circles with increasing radii.
The circles are drawn in sequence, starting from a radius of 10 and doubling in size with each subsequent circle.
"""

"""这段代码使用了Python的turtle模块来绘制一系列的圆形。turtle模块是Python标准库中的一个图形绘制工具，它提供了一个简单的接口来创建图形和动画。

首先，代码通过import turtle导入了turtle模块。接着，turtle.pensize(2)设置了画笔的宽度为2个单位，这会影响之后绘制的所有图形的线条粗细。
"""
import turtle
turtle.pensize(2)

"""然后，代码连续调用了四次turtle.circle()方法来绘制圆形。每次调用turtle.circle()时，都会传入一个参数，表示要绘制的圆的半径。这四次调用分别绘制了半径为10、40、80和160单位的圆形。由于没有指定圆心的位置，这些圆形都是以turtle模块默认的起始位置（通常是屏幕中心）为中心绘制的。

这段代码的执行结果是，在屏幕上绘制了四个同心圆，它们的半径依次增大。这种简单的图形绘制可以帮助初学者理解turtle模块的基本用法，同时也是学习编程可视化的一个很好的起点。
"""

turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)

"""如果你想要改进这段代码，可以考虑添加一些交互性，比如让用户输入圆的半径，或者绘制更多不同大小和颜色的圆形。此外，使用循环结构可以避免重复代码，例如：
import turtle
turtle.pensize(2)
radii = [10, 40, 80, 160]
for radius in radii:
    turtle.circle(radius)
这样，如果你想要改变绘制的圆形数量或者它们的半径，只需要修改radii列表中的值即可。
"""