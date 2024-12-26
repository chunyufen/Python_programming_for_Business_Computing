# Week-2/HowMuchExchangeAdvance.py
"""如果你在一家零售店幫消費的客人結帳，你可能需要快速地挑出合適且數量正確的鈔票與零錢。假設客人的消費金額 a 一定是 1 到 1000 之間的整數，而你有無限量的 500、100、50、10、5、1 這些面額的鈔票和零錢，我們希望你能依照下面的規則找錢：

1. 你找的錢的總額要是 1000 - a。

2. 與其給客人五張 100 元，不如給他一張 500 元；與其給客人兩個 50 元，不如給他一張 100 元……依此類推。

以下是一些範例：

1. 如果客人消費 200 元，你應該找給他 1 張 500 元和 3 張 100 元。
2. 如果客人消費 286 元，你應該找給他 1 張 500 元、2 張 100 元、1 個 10 元和 4 個一元。
3. 如果客人消費 925 元，你應該找給他 1 個 50 元、2 個 10 元和 1 個 5 元。

在本題中，你將會被給予上述的整數 a，而你要找出符合上述規則的唯一找錢方式。但如果不應該找給客人某個面額的鈔票或銅板，就跳過該面額不要輸出。因為這樣一來可能只輸出少於 6 個數字，會不知道怎麼對應到面額，因此現在要把面額與所需張數（個數）成對地輸出，中間用一個逗點和一個空格隔開，而面額與面額之間用一個分號和一個空格隔開。
"""



a = int(input("How much did the customer spent? ")) # money spent
balance = 1000 - a 

five_hundred = balance // 500
if five_hundred == 0:
    pass
else:
    text_500 = f"500, {five_hundred};"
    print(text_500, end="")

balance = balance % 500
one_hundred = balance // 100
if one_hundred == 0:
    pass
else:
    text_100 = f"100, {one_hundred};"
    print(" " + text_100, end="")

balance = balance % 100
fifty = balance // 50
if fifty == 0:
    pass
else:
    text_50 = f"50, {fifty};"
    print(" " + text_50, end="")

balance = balance % 50
ten = balance // 10
if ten == 0:
    pass
else:
    text_10 = f"10, {ten};"
    print(" " + text_10, end="")
    
balance = balance % 10
five = balance // 5
if five == 0:
    pass
else:
    text_5 = f"5, {five};"
    print(" " + text_5, end="")
    
balance = balance % 5
one = balance // 1
if one == 0:
    pass
else:
    text_1 = f"1, {one};"
    print(" " + text_1, end="")




