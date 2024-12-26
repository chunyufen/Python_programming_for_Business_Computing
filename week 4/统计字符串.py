# week 4/统计字符串.py


str1 = input("请输入一行字符串：")

alpha = 0  # 英文字母
space = 0  # 空格
digit = 0  # 数字
other = 0  # 其他

for char in str1:
    if char.isalpha():
        alpha += 1
    elif char.isspace():
        space += 1
    elif char.isdigit():
        digit += 1
    else:
        other += 1

print(f"{str1} 中的英文字母个数为：{alpha}")
print(f"{str1} 中的空格个数为：{space}")
print(f"{str1} 中的数字个数为：{digit}")
print(f"{str1} 中的其他字符个数为：{other}")

exit()