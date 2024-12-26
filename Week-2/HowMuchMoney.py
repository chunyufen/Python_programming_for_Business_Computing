# Week-2/HowMuchMoney.py
# 你手上有面額 50、10、5、1 元的銅板各w、x、y、z 個，請計算你一共有多少錢。

# this program gives correct answer

fifty = int(input("請輸入50元銅板數量: "))
ten = int(input("請輸入10元銅板數量: "))
five = int(input("請輸入5元銅板數量: "))
one = int(input ("請輸入1元銅板數量: "))
money = fifty * 50 + ten * 10 + five * 5 + one * 1
print(money)

