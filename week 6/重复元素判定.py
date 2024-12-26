# week6/重复元素判定.py

# 重复元素判定。编写⼀个函数，接受列表作为参数，
# 如果⼀个元素在列表中出现了不⽌⼀次，则返回True，
# 但不要改变原来列表的值。同时编写调⽤这个函数和测试结果的程序

def duplic(lst):
    for i in lst:
        if (lst.count(i) >= 2):
            print("True")
            break


lst1 = [123123, 23123, '123123', [123], (123), 123]
duplic(lst1)

