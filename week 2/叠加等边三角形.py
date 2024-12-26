# week 2/叠加等边三角形.py

"""首先，代码导入了turtle模块，并给它起了一个别名t，这样就可以用t来代替整个turtle模块，使得代码更加简洁。

2. 然后，代码通过input函数提示用户输入三角形的边长，并将输入的字符串转换为整数类型，存储在变量side_length中。这个边长值将用于后续绘制三角形时的移动距离。

3. 接下来，代码使用了一个for循环，循环3次，每次循环中，turtle会向前移动side_length的距离，然后向右转120度。因为等边三角形的每个内角都是60度，所以转120度可以保证turtle回到起点并完成三角形的绘制。

4. 绘制完第一个三角形后，turtle向左转60度，这是为了准备绘制第二个三角形。接着，turtle再次向前移动side_length的距离，这次是为了将第二个三角形的底边与第一个三角形的顶点对齐。

5. 又是一个for循环，循环3次，这次每次循环中，turtle先向右转120度，然后向前移动side_length*2的距离。这样做的目的是绘制出一个边长是第一个三角形两倍的等边三角形。

6. 最后，代码调用了t.hideturtle()来隐藏turtle的箭头图标，使得绘制的图形更加清晰。然后调用t.done()来结束turtle的绘图窗口。


"""


import turtle as t

side_length = int(input("Please enter the length of the triangle: "))  # 100

for i in range(3):
    t.fd(side_length)
    t.right(120)
    
t.left(60)
t.fd(side_length)
for i in range(3):
    t.right(120)
    t.fd(side_length*2)
    
t.hideturtle()
t.done()
