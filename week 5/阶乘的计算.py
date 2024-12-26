# week 5/阶乘的计算.py

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
n = eval(input("请输入一个整数: "))
print(factorial(abs(int(n))))

# abs(int(n)) 这部分代码首先将变量 n 转换为整数类型（int(n)），然后取其绝对值（abs(...)）。这样做是为了确保即使 n 是负数或者是一个可以转换为整数的字符串，factorial 函数也能接收到一个非负整数作为参数。阶乘函数通常只定义在非负整数上。