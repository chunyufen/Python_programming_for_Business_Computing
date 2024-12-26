# week 4/猜数字游戏.py

import random

# 猜数字游戏
# 随机预测一个数

"""用random函数随机预设一个0～100之间的整数，for循环控制输入的次数，使用异常处理非法输入时的错误。"""

answer = random.randint(1, 101)
# 循环控制次数
for i in range(1, 101):
    try:
        a = int((input("请输入你心中的数字:")))
        if a > answer:
            print("遗憾，太大了")
        elif a == answer:
            print("预测", i, "次，恭喜你猜中了!")
            break
        elif a < answer:
            print("遗憾，太小了")
    except:
        print("输入内容必须为整数，请重新输入!")

