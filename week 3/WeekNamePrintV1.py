# week 3/WeekNamePrintV1.py

"""This script takes a number input from the user, representing a day of the week (1-7), and prints the corresponding Chinese day name from the string `weekStr`. The calculation for the position in the string is based on the input number, with each day name being 3 characters long.
"""
weekStr = "星期一星期二星期三星期四星期五星期六星期日"  # 首先，定义了一个字符串weekStr，它包含了按顺序排列的星期一到星期日的中文名称，每个名称之间没有空格。
weekId = eval(input("请输入星期数字(1-7)："))  # 然后，代码使用input函数提示用户输入一个数字（1-7），代表星期一到星期日。eval函数用于将用户输入的字符串转换为整数。
pos = (weekId - 1 ) * 3  # 接下来，计算字符串中对应星期名称的起始位置。由于每个星期的名称由三个中文字符组成，所以通过(weekId - 1) * 3计算出起始位置的索引。这里weekId - 1是因为字符串索引是从0开始的，而星期数字是从1开始的。
print(weekStr[pos: pos+3])  # 最后，使用字符串切片功能weekStr[pos: pos+3]来获取并打印出从pos位置开始的三个字符，即对应的星期名称。
"""
需要注意的是，这段代码使用了eval函数，这可能会带来安全风险，因为eval会执行传入的字符串，如果用户输入恶意代码，可能会导致程序崩溃或其他安全问题。在实际应用中，应该使用更安全的方法来转换用户输入，例如使用int函数，并且添加异常处理来确保输入的有效性。

此外，这段代码假设用户输入的数字总是在1到7之间，没有进行错误检查。在实际应用中，应该添加适当的输入验证来确保程序的健壮性。
"""