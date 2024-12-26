# week 3/TextProBarV2.py
"""This script displays a simple text-based progress bar that updates every 0.1 seconds, incrementing from 0% to 100%. It uses a for loop with the range function and the print function with carriage return to overwrite the current line, creating the illusion of a progressing bar.
"""
import time  # import time：这一行导入了time模块，该模块提供了各种与时间相关的功能，包括暂停程序执行的sleep函数。
for i in range(101):  # for i in range(101):：这是一个从0到100的循环，代表进度条的百分比。range(101)会生成一个包含0到100的整数序列。 
    print("\r{:3}%".format(i), end=" ")  # print("\r{:3}%".format(i), end=" ")：这一行代码负责打印进度条。\r是一个特殊的转义字符，它会使光标回到行首，这样下一次打印时就会覆盖掉上一次的内容，从而实现进度条的动态更新效果。{:3}是一个格式化占位符，它告诉Python将变量i的值格式化为至少3个字符宽度的字符串，不足的部分会在前面补空格，这样可以保证进度条的对齐。%是进度条的符号。format(i)将变量i的值插入到占位符中。end=" "参数告诉print函数在打印结束后不要换行，而是在同一行输出一个空格。
    time.sleep(0.1)  # time.sleep(0.1)：这一行代码使程序暂停执行0.1秒。这样做是为了减慢进度条的更新速度，使其对用户可见。