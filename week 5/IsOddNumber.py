# week 5/IsOddNumber.py

def isOdd(num):
    try:
        if type(num) == type(0.):
            raise TypeError
        if num%2 == 0:
            return False
        else:
            return True
    except TypeError:
        print('这不是一个有效的整数！')

# 测试集

print(isOdd(4))  # False
print(isOdd(3))  # True
print(isOdd(-1))  # True
print(isOdd('str'))  # 这不是一个有效的整数！
print(isOdd(3.))  # 这不是一个有效的整数！