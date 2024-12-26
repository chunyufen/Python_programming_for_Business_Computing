# week 5/SevenDigitsDrawV1.py
"""This script uses the turtle graphics module to draw a digital representation of a date. The `drawDigit` function draws individual digits based on the turtle's current position and orientation. The `drawDate` function iterates over a string representing a date, calling `drawDigit` for each character. The `main` function sets up the turtle environment, positions the turtle, and initiates the drawing process for a specific date.
"""
import turtle
def drawLine(draw):  # 首先，定义了一个名为drawLine的函数，它接受一个布尔值draw作为参数。如果draw为True，乌龟会放下笔开始绘制，并向前移动40个单位，然后向右转90度；如果draw为False，乌龟会抬起笔移动，不留下痕迹。
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit):  # 接下来是drawDigit函数，它负责绘制单个数字。这个函数通过一系列的条件判断来决定是否调用drawLine函数，从而绘制出数字的各个部分。这里的数字是通过turtle模块的标准绘图命令来表示的，每个数字由7条线段组成。
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):  # drawDate函数接受一个日期字符串作为参数，然后将字符串中的每个字符（假设是数字）转换为整数，并调用drawDigit函数来绘制对应的数字。
    for i in date:
        drawDigit(eval(i))
def main():  # 最后，main函数设置了turtle窗口的大小和位置，并通过一系列的命令将乌龟移动到合适的位置开始绘制。然后调用drawDate函数来绘制日期'20181010'。绘制完成后，隐藏了乌龟图标，并通过turtle.done()结束绘图。
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20181010')
    turtle.hideturtle()
    turtle.done()
main()
"""需要注意的是，代码中使用了eval(i)来将字符转换为整数，这在实际编程中是不安全的做法，因为它会执行传入的字符串作为代码，这里应该使用int(i)来进行安全的类型转换。

此外，代码的可读性可以通过添加注释和使用更具描述性的变量名来提高。例如，drawLine函数的参数名draw可以改为should_draw，以更清楚地表明其作用。
"""