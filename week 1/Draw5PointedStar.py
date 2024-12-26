# week 1/Draw5PointedStar.py
"""This script uses the turtle graphics module to draw a filled, five-pointed star with a yellow outline and red fill color. The star is created by moving forward by 200 units and turning right by 144 degrees in a loop that repeats five times, encapsulating the drawing commands within begin_fill() and end_fill() to fill the star with the specified color.
"""

from turtle import *  # from turtle import *：这行代码导入了turtle模块中的所有函数和类，使得我们可以在代码中直接使用turtle模块提供的绘图功能。
color('yellow','red')  # color('yellow','red')：这行代码设置了绘制五角星时的填充颜色和边框颜色。第一个参数'yellow'是填充颜色，第二个参数'red'是边框颜色
begin_fill()  # begin_fill()：这个函数调用告诉turtle开始记录路径，以便之后用end_fill()函数填充颜色。在调用begin_fill()和end_fill()之间的路径将被填充上之前设置的颜色。
for i in range(5):  # for i in range(5):：这是一个for循环，它会执行5次，因为range(5)生成了一个从0到4的序列。这个循环用来绘制五角星的每一条边。
    fd(200)  # fd(200)：在循环内部，fd是forward的缩写，它让turtle向前移动200个单位长度。这行代码在每次循环中都会执行，用于绘制五角星的每一条边。
    rt(144)  # rt(144)：rt是right的缩写，它让turtle向右转144度。五角星的每个内角是36度，所以外角是180-36=144度。这行代码确保turtle在绘制完一条边后转向正确的角度以绘制下一条边。
end_fill()  # end_fill()：这个函数调用告诉turtle结束填充路径。在begin_fill()和end_fill()之间的路径将被填充上之前设置的颜色。
done()  # done()：这个函数调用结束turtle的绘图会话。在这之后，turtle窗口将保持打开状态，直到用户关闭它。
