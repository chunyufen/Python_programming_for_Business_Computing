# week 1/太阳花的绘制.py

from turtle import *
color('red','yellow')
begin_fill()
while 1:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()