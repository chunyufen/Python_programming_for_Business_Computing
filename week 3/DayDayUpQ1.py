# week 3/DayDayUpQ1.py

"""This script calculates the growth and decay factors over a year, assuming a daily increase of 1.001% and a daily decrease of 0.999%. It prints the results formatted to two decimal places.
"""

dayup = pow(1.0 + 0.001, 365)  # 首先，变量dayup通过pow(1.001, 365)计算了每天进步1%的效果。这里的1.001代表每天增长的比例，而365是一年的天数。这意味着如果每天都比前一天多出1%，那么一年后的增长效果就是dayup的值。
daydown = pow(1.0 - 0.001, 365)  # 接着，变量daydown通过pow(0.999, 365)计算了每天退步1%的效果。这里的0.999代表每天减少的比例，同样地，365是一年的天数。这意味着如果每天都比前一天少了1%，那么一年后的减少效果就是daydown的值。
print("向上:{:.2f}, 向下:{:.2f}".format(dayup, daydown))  # 最后，代码使用print函数打印出这两个结果。这里使用了字符串格式化方法.format()来插入dayup和daydown的值到打印的字符串中，并且指定了保留两位小数。
# 或者使用f-string：
# print(f"向上:{dayup:.2f}, 向下:{daydown:.2f}")