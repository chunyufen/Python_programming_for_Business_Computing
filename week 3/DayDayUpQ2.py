# week 3/DayDayUpQ2.py

"""This script calculates the compounded growth and decay over a year, given a daily factor.
- `dayfactor`: The daily growth or decay factor.
- `dayup`: The result of compounding growth over 365 days.
- `daydown`: The result of compounding decay over 365 days.
"""

# 首先，变量dayfactor被设置为0.005，这代表了每天的增长率或衰减率。接着，使用pow函数计算了在365天后，这个因子累积增长的效果，存储在变量dayup中。同样地，也计算了每天减少这个因子后的累积效果，存储在变量daydown中。
# 最后，使用print函数输出了这两个值，格式化为两位小数。输出的字符串是中文，分别表示向上增长和向下衰减的结果。
# 这段代码的一个关键点是它展示了复利效应，即每天的增长或减少都是在前一天的基础上进行的。这在金融计算中很常见，比如计算利息或者投资回报率。
# 此外，这段代码使用了Python的内置函数pow来进行幂运算，这是一种快速计算幂的方法。在这里，pow(1+dayfactor, 365)计算的是(1 + dayfactor)的365次方，而pow(1-dayfactor, 365)计算的是(1 - dayfactor)的365次方。
# 如果这段代码是为了教学目的，它很好地展示了指数增长和衰减的概念。如果用于实际应用，可能需要考虑更精确的数学库来处理浮点数的精度问题。
dayfactor = 0.005
dayup = pow(1.0 + dayfactor, 365)
daydown = pow(1.0 - dayfactor, 365)
print("向上:{:.2f}, 向下:{:.2f}".format(dayup, daydown))