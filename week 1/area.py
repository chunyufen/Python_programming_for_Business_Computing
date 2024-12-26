# week 1/Area.py
"""This script calculates the area of a circle given its radius. The radius is set to 25, and the area is computed using the formula πr², where π is approximated as 3.1415. The result is printed twice: once with full precision and once rounded to two decimal places.
"""
r = 25
area = 3.1415 * r * r  # 代码使用 print 函数输出了计算得到的面积值。这是第一次输出，显示的是圆面积的完整小数形式。
print(area)  # 代码再次使用 print 函数，但这次使用了字符串格式化方法 format 来输出圆面积，并保留了两位小数。这种方法可以让输出的数字更加整洁易读。 
print("{:.2f}".format(area)) 