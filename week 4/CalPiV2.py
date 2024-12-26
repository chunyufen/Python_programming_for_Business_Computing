# week 4/CalPiV2.py
"""This script calculates an approximation of Pi using the Monte Carlo method. It simulates throwing darts at a unit circle and counts the number of darts that land within the circle to estimate Pi. The script measures the time taken to perform the calculation.
"""
from random import random  # 首先，代码从random模块导入random函数，用于生成0到1之间的随机浮点数，以及从time模块导入perf_counter函数，用于测量程序运行的时间。
from time import perf_counter
DARTS = 10000000  # 定义了一个常量DARTS，表示将要投掷的飞镖数量，这里设置为10000000。变量hits初始化为0.0，用来记录落在单位圆内的飞镖数量。
hits = 0.0
start = perf_counter()  # 接下来，调用perf_counter()函数开始计时。然后进入一个for循环，循环次数为DARTS，即投掷飞镖的次数。在每次循环中，使用random()函数生成两个随机数x和y，这两个数分别代表飞镖在单位正方形内的横纵坐标。通过计算点(x, y)到原点的距离dist（使用勾股定理），并与1.0比较，来判断这个点是否落在以原点为中心，半径为1的单位圆内。如果dist小于或等于1.0，说明飞镖落在了单位圆内，hits的值就增加1。
for i in range (1, DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)  # 循环结束后，通过公式4 * (hits / DARTS)来估算π的值。这是因为单位圆的面积是π，而单位正方形的面积是4，通过比较两者内的随机点数量，可以估算出π的值。
print("pi的值是{}".format(pi))  # 最后，打印出估算出的π值和程序运行的时间。注意，perf_counter()函数返回的是程序运行的处理器时间，而不是实际的墙钟时间。
print("运行的时间是{:5.5}s".format(perf_counter() - start))