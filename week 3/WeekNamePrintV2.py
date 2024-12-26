# week 3/WeekNamePrintV2.py

"""This script prompts the user to input a number from 1 to 7, representing the days of the week.
It then prints out the corresponding day in Chinese using a string mapping.
Note: The use of `eval` for input is not recommended due to security risks; consider using `int(input())` instead.
"""
weekStr = "一二三四五六日"  # weekStr = "一二三四五六日" 这行代码定义了一个字符串变量weekStr，它包含了星期的中文名称，从星期一到星期日。
weekId = eval(input("请输入星期数字(1-7)："))  # weekId = eval(input("请输入星期数字(1-7)：")) 这行代码提示用户输入一个数字，代表星期几（1代表星期一，7代表星期日）。input()函数用于获取用户的输入，而eval()函数则将输入的字符串转换为相应的数值。需要注意的是，使用eval()可能存在安全风险，因为它会执行传入的字符串，如果用户输入恶意代码，可能会造成程序崩溃或其他安全问题。在实际应用中，建议使用更安全的方法来转换输入，例如int()函数，并添加异常处理来确保输入的有效性。
print("星期" + weekStr[weekId-1])  # print("星期" + weekStr[weekId-1]) 这行代码首先打印出“星期”两个字，然后通过字符串索引的方式从weekStr中取出对应的星期名称并打印出来。由于字符串索引是从0开始的，而用户输入的星期数字是从1开始的，所以需要用weekId-1来获取正确的索引值。