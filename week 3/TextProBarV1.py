# week 3/TextProBarV1.py

"""This script displays a simple text-based progress bar that fills up over a specified scale (10 in this case). It prints the percentage completion along with the visual representation of the progress using asterisks (*) for completed parts and dots (.) for the remaining part. The progress bar updates every 0.1 seconds, simulating a long-running process.

Parameters:
- scale (int): Determines the total length of the progress bar.

Usage:
Run the script to see the progress bar in action, which will complete in 1 second given the scale of 10 and sleep interval of 0.1 seconds.
"""
import time  # 这行代码导入了time模块，它提供了各种与时间相关的功能，这里主要用到了sleep函数来让程序暂停执行一段时间。
scale = 10  # 这行代码定义了一个变量scale，它的值为10。这个变量决定了进度条的总长度，即进度条将分为10个部分。
print("------执行开始------")  # 这行代码打印出进度条开始执行的消息。
for i in range(scale+1):  # 这是一个for循环，它会遍历从0到scale（包含scale）的所有整数。这意味着循环将执行scale+1次，这里是11次。
    a = '*' * i  # 在循环内部，这行代码创建了一个字符串a，它由i个星号（*）组成。随着循环的进行，i的值会增加，因此字符串a的长度也会增加，表示进度条的填充部分。
    b = '.' * (scale - i)  # 这行代码创建了另一个字符串b，它由scale - i个点（.）组成。这个字符串代表进度条中未填充的部分。
    c = (i/scale) * 100  # 这行代码计算了当前进度的百分比。i/scale计算了当前步骤占总步骤的比例，乘以100将其转换为百分比。
    print("{:^3.0f}%[{}->{}]".format(c,a,b))  # 这行代码打印出进度条的当前状态。{:^3.0f}是一个格式化字符串，它将变量c的值居中显示，并保留0位小数，即显示为整数。%后面跟着的是进度百分比，[{}->{}]中的大括号会被变量a和b的值替换，分别代表进度条的填充部分和未填充部分。
    time.sleep(0.1)  # 这行代码让程序暂停执行0.1秒。这样做是为了让进度条的显示更加平滑，给用户一种进度逐渐增加的感觉。
print("------执行结束------")  # 当循环结束后，这行代码打印出进度条执行结束的消息。

