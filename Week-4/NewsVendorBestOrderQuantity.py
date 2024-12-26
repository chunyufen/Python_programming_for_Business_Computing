# Week-4/NewsVendorBestOrderQuantity.py

"""This script calculates the optimal order quantity for a news vendor problem using a probabilistic approach. It takes inputs for unit cost, retail price, and possible demand quantities. Then, it prompts for the probability of selling each quantity from 0 to N. The script iterates through possible order quantities, calculating the expected profit for each and determines the quantity that yields the maximum profit.
"""
# https://josh24311.blogspot.com/2018/11/python.html

import math

c = int(input("單位進貨成本是多少？"))
r = int(input("單位零售價格是多少？"))
N = int(input("需求的可能個數是多少？")) # 題目說8份


plist = []
plist.append(float(input("賣掉0份的機率會是多少?")))
plist.append(float(input("賣掉1份的機率會是多少?")))
plist.append(float(input("賣掉2份的機率會是多少?")))
plist.append(float(input("賣掉3份的機率會是多少?")))
plist.append(float(input("賣掉4份的機率會是多少?")))
plist.append(float(input("賣掉5份的機率會是多少?")))
plist.append(float(input("賣掉6份的機率會是多少?")))
plist.append(float(input("賣掉7份的機率會是多少?")))
plist.append(float(input("賣掉8份的機率會是多少?")))


exp = 0 # 該進貨量下之預期收益
sum = 0.0 # original sum = 0.0
D = 0.0
maxP = 0.0 # 最大利潤
qMax = 0 # 可達最大利潤之進貨數
# N = 8


for q in range(0,N+1) :
  sum = 0.0
  D = 0.0
  for p in range(0,q+1) :
  # p 為 不大於進貨量下之需求量
    exp = r * min(p,q) - c * q
    if p != q :
      sum += plist[p] * exp
      D += plist[p]
    else:
      sum += (1-D) * exp
      break
  if sum > maxP :
    maxP = sum # 賣出最佳訂購量之利潤 maxP
    qMax = q
 
profit = int(maxP)
print(str(qMax)+" "+str(profit)) # 最佳訂購量 # 在此訂購量下的預期利潤

# 4, 18 after moving line 46 to 48 to the lef leaving 1 column blank on the left; answer says 4 18
# 0, 0
# 4, 86
# 3, 37
# 4, 117
# 8, 586