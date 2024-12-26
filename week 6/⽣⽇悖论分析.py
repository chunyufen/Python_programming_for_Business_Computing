# week 6/⽣⽇悖论分析.py


# ⽣⽇悖论指如果⼀个房间⾥有23⼈或以上，那么至少有两个⼈⽣⽇相同的概率⼤于50%。
# 编写程序，输出在不同随机样本数量下，23个⼈中至少两个⼈⽣⽇相同的概率

from random import randint

prsnum = eval(input("请输入房间人数："))
times = 100000
percent = 0
for t in range(times):
    person = []
    for pn in range(prsnum):
        person.append(randint(1, 366))
    for pn in person:
        if person.count(pn) >= 2:
            percent += 1
            break

print("概率为{:.2%}".format(percent/times))