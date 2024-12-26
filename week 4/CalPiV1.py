# week 4/CalPiV1.py
"""This script calculates an approximation of Pi using the Leibniz formula for π/4.
It iterates N times, summing the terms of the series to estimate π.
"""
pi = 0  # pi = 0：初始化圆周率的估计值为0。
N = 100  # N = 100：设置迭代次数为100，这个数字决定了估算的精度。迭代次数越多，计算出的圆周率值越精确。
for K in range(N):  # for K in range(N):：这是一个循环，它会执行N次，其中K的值从0到99。
    pi += 1/pow(16,K)*(4/(8*K+1)-2/(8*K+4)-1/(8*K+5)-1/(8*K+6))  # 在循环内部，pi += 1/pow(16,K)*( 开始了一个表达式，用于更新圆周率的值。这里使用了pow(16,K)来计算16的K次幂，这里的K是一个循环变量，它会从0开始逐渐增加。4/(8*K+1)、-2/(8*K+4)、-1/(8*K+5) 和 -1/(8*K+6) 这四个分数是级数中的项，它们随着K的增加而变化。这些分数被乘以 1/pow(16,K)，然后加到 pi 上，是莱布尼茨级数的一个特例，它通过一系列分数的和来逼近圆周率。
print("圓周率是{}".format(pi))  # print("圓周率是{}".format(pi))：在循环结束后，打印出估算出的圆周率值。注意，这里使用了format()函数来格式化输出，其中{pi}表示pi的值，可以用{:.5f}表示小数点后保留5位小数。