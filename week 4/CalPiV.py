# week 4/CalPiV.py
"""This script calculates an approximation of Pi using the Monte Carlo method. It simulates throwing darts at a unit circle inscribed within a square. The ratio of darts that land inside the circle to the total number of darts thrown is used to estimate Pi. The script also measures and prints the execution time.
"""
from random import random  # 首先，代码从random模块导入random函数，用于生成随机数；从math模块导入sqrt函数，用于计算平方根；从time模块导入clock函数，用于计时。
from math import sqrt
from time import clock
DARTS = 10000  # 定义了一个常量DARTS，表示将要投掷的飞镖数量，这里设置为10000。变量hits初始化为0.0，用来记录落在单位圆内的飞镖数量。
hits =0.0
clock()  # 接下来，调用clock()函数开始计时。然后进入一个for循环，循环次数为DARTS，即投掷飞镖的次数。在每次循环中，使用random()函数生成两个随机数x和y，这两个数分别代表飞镖在单位正方形内的横纵坐标。通过计算点(x, y)到原点的距离dist（使用勾股定理），并与1.0比较，来判断这个点是否落在以原点为中心，半径为1的单位圆内。如果dist小于或等于1.0，说明飞镖落在了单位圆内，hits的值就增加1。
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = sqrt(x**2+y**2)
    if dist<=1.0:
        hits +=1
pi = 4*(hits/DARTS)  # 循环结束后，通过公式4 * (hits / DARTS)来估算π的值。这是因为单位圆的面积是π，而单位正方形的面积是4，通过比较两者内的随机点数量，可以估算出π的值。
print("pi的值是{}".format(pi))  # 最后，打印出估算出的π值和程序运行的时间。注意，clock()函数返回的是程序运行的处理器时间，而不是实际的墙钟时间。
print("运行的时间是{:5.5}s".format(clock()))
"""这段代码的一个潜在问题是，它使用了Python 2的clock()函数，在Python 3中已经被废弃，应该使用time.perf_counter()或者time.process_time()来代替。

此外，代码中的变量hits应该初始化为整数0而不是浮点数0.0，因为在循环中hits的值只会增加整数1，不需要用到浮点数。

代码的可读性可以通过添加注释和更具描述性的变量名来提高，例如将hits改为hit_count，将DARTS改为num_darts等。
"""