# Week-2/HowMuchExchange.py
"""如果你在一家零售店幫消費的客人結帳，你可能需要快速地挑出合適且數量正確的鈔票與零錢。假設客人的消費金額 a 一定是 1 到 1000 之間的整數，而你有無限量的 500、100、50、10、5、1 這些面額的鈔票和零錢，我們希望你能依照下面的規則找錢：

1. 你找的錢的總額要是 1000 - a。

2. 與其給客人五張 100 元，不如給他一張 500 元；與其給客人兩個 50 元，不如給他一張 100 元……依此類推。

以下是一些範例：

1. 如果客人消費 200 元，你應該找給他 1 張 500 元和 3 張 100 元。
2. 如果客人消費 286 元，你應該找給他 1 張 500 元、2 張 100 元、1 個 10 元和 4 個一元。
3. 如果客人消費 925 元，你應該找給他 1 個 50 元、2 個 10 元和 1 個 5 元。

在本題中，你將會被給予上述的整數 a，而你要找出符合上述規則的唯一找錢方式。
"""



a = int(input("How much did the customer spent? ")) # money spent
balance = 1000 - a # so exchange is 

five_hundred = balance // 500
print(f"{five_hundred} five-hundred-dollar bill.")

balance = balance % 500
# print(balance)
one_hundred = balance // 100
print(f"{one_hundred} one-hundred-dollar bill.")

balance = balance % 100
# print(balance)
fifty = balance // 50
print(f"{fifty} fifty-dollar bill.")


balance = balance % 50
# print(balance)
ten = balance // 10
print(f"{ten} ten-dollar bill.")

balance = balance % 10
# print(balance)
five = balance // 5
print(f"{five} five-dollar bill.")

balance = balance % 5
one = balance // 1
print(f"{one} one-dollar bill.")
print(f"{five_hundred}, {one_hundred}, {fifty}, {ten}, {five}, {balance}")