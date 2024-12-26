# Week-4/NewsVendorExpectedProfitV2.py
# --------------------
# This program gives the correct answer
# --------------------
# https://josh24311.blogspot.com/2018/11/python.html

"""This script calculates the expected profit for a news vendor based on the given costs, revenues, demand probabilities, and quantities. It takes user inputs for fixed costs (c), revenue per unit (r), total units (q), and number of demand scenarios (N). Then, it prompts for the probability of each demand scenario. The script computes the expected profit by iterating through each possible quantity sold, calculating the profit for each scenario, and summing them up.
"""
import math

c = int(input("單位進貨成本是多少？"))
r = int(input("單位零售價格是多少？"))
N = int(input("需求的可能個數是多少？")) # 題目說8份
q = int(input("訂貨量是多少？"))

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

# can be replaced by the following:
"""
 plist = [float(input("賣掉0份的機率會是多少?")), float(input("賣掉1份的機率會是多少?")),
         float(input("賣掉2份的機率會是多少?")), float(input("賣掉3份的機率會是多少?")),
         float(input("賣掉4份的機率會是多少?")), float(input("賣掉5份的機率會是多少?")),
         float(input("賣掉6份的機率會是多少?")), float(input("賣掉7份的機率會是多少?")),
         float(input("賣掉8份的機率會是多少?"))]
"""

exp = 0
sum = 0.0
D = 0.0
maxP = 0

for p in range(0,q+1) :
    exp = r * p - c * q
    if p != q :
        sum += plist[p] * exp
        D += plist[p]
    else :
        sum += (1-D) * exp
        break

print(int(sum))

# 13
# 22
# 26