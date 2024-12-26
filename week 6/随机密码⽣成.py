# week 6/随机密码⽣成.py

# 随机密码⽣成。编写程序，在26个字母⼤⼩写和9个数字组成的列表中随机⽣成10个8位密码

from random import sample

lst1 = []
for i in range(49, 58):
    lst1.append(chr(i))
for c in range(97, 123):
    lst1.append(chr(c))
# print(lst1)

for p in range(10):
    print("".join(sample(lst1, 8)))