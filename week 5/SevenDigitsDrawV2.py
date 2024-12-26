# week 5/SevenDigitsDrawV2.py
"""This script uses the turtle graphics library to draw a seven-segment digital tube display for dates. The `drawDigit` function draws individual digits based on a boolean representation of which segments should be lit. The `drawDate` function interprets a string formatted as 'YYYYMMDD' and draws each digit with appropriate separators ('年', '月', '日') in different colors. The `main` function sets up the turtle environment and initiates the drawing process.
"""
import turtle, datetime  # 这段代码是一个使用Python的turtle模块来绘制七段数码管的程序。它的主要功能是根据输入的日期字符串来绘制相应的数码管表示。首先，代码定义了几个函数来绘制数码管的各个部分： 
def drawGap():  # drawGap() 函数用于绘制数码管之间的间隔，它会使画笔抬起并向前移动5个单位。
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):  # drawLine(draw) 函数用于绘制数码管的一段，参数draw决定是否实际绘制线条。如果draw为真，则画笔落下并向前移动40个单位；如果为假，则只抬起画笔移动。
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit):  # drawDigit(digit) 函数根据输入的数字绘制整个七段数码管。它通过调用drawLine()函数七次来绘制数码管的七段，每段是否绘制取决于数字的值。
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
def drawDate(date):  # drawDate(date) 函数用于绘制整个日期。它遍历日期字符串中的每个字符，如果是分隔符（'-'、'='、'+'），则绘制相应的中文字符（年、月、日）并改变画笔颜色；如果是数字，则调用drawDigit()函数来绘制对应的数码管。
    turtle.pencolor("red")
    for i in date:
        if i=='-':
            turtle.write('年',font = ('Arial',18,'normal'))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font =("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))

def main():  # 最后，main() 函数设置了turtle窗口的大小和起始位置，并调用drawDate()函数来绘制日期'20181010'。绘制完成后，隐藏画笔并结束turtle绘图。
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20181010')
    turtle.hideturtle()
    turtle.done()
main()
"""这段代码的一个注意点是，它使用了eval()函数来将字符转换为数字。这在处理用户输入时是不安全的，因为它可以执行任意代码。在这个特定的例子中，由于输入是硬编码的日期字符串，风险较低，但在实际应用中应避免使用eval()。

此外，代码中的颜色变化是通过改变turtle.pencolor()来实现的，这为绘制增添了一些视觉效果。
"""