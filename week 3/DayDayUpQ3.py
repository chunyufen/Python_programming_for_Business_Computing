# week 3/DayDayUpQ3.py

"""This script calculates the growth of an initial value over 365 days, taking into account a weekly decrease on weekends.
- `dayup`: The initial value that grows daily.
- `dayfactor`: The daily growth factor, applied on weekdays and a decrease factor on weekends.
- The loop iterates over each day of the year, adjusting `dayup` based on whether it's a weekday or weekend.
- The final value of `dayup` is printed, demonstrating the cumulative effect of daily growth and weekend decrease.
"""

# 这段代码是一个简单的Python程序，用于计算一个人如果每天都比前一天稍微努力一点，一年后的成就会有多大。这里的“努力”被量化为一个增长因子，而周末则假设为不努力的日子，会有一个减少因子。


dayup = 1.0  # 首先，定义了两个变量：dayup和dayfactor。dayup代表每天的成就值，初始值为1.0；dayfactor是每天努力带来的增长因子，设定为0.01。这意味着在非周末的日子里，每天的成就值会增长1%。
dayfactor = 0.01
for i in range(365):  # 接下来，代码使用了一个for循环，循环365次，代表一年的365天。在循环内部，使用了一个if语句来检查当前的天数是否是周末（即星期六或星期日）。这是通过i % 7来计算的，因为一周有7天，所以任何天数除以7的余数可以表示是周几。余数为6代表星期六，余数为0代表星期日。
    if i % 7 in [6, 0]:  # 如果当前天是周末，那么dayup的值会乘以(1 - dayfactor)，即减少了1%。如果不是周末，dayup的值则会乘以(1 + dayfactor)，即增加了1%。
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("工作日的力量：{:.2f}".format(dayup))  # 最后，循环结束后，使用print函数输出最终的成就值，格式化为两位小数，并附带一条消息“工作日的力量：”，表明这个值是由工作日的努力累积而成的。