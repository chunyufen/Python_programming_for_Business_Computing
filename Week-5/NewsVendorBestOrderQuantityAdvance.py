# Week-5/NewsVendorBestOrderQuantityAdvance.py

# https://jamie-life-coding.medium.com/python-%E5%95%86%E7%AE%A1%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E5%BF%83%E5%BE%97-%E4%B8%8B-6a8dfac006f2

"""
成本:5
售价:10
需求函数个数:5
残值:1

第0 个需求机率:0.2
第1个需求机率:0.15
第2 个需求机率:0.15
第3个需求机率:0.2
第4个需求机率:0.18
第5个需求机率:0.12

函数值加总为1
[0.2, 0.15, 0.15, 0.2, 0.18, 0.12]

购买0个的期望利润为:0.0
购买1个的期望利润为:3.2    # 0-5+1=-4 10-5+0=5 (-4)*0.2+5*0.8=4-0.8=3.2
购买2个的期望利润为:5.05
购买3个的期望利润为:5.549999999999999
购买4个的期望利润为:4.250000000000001
购买5个的期望利润为:1.3300000000000027

最佳期望数量:3
期望利润为:5
"""

c = int(input())
r = int(input())
N = int(input())
s = int(input())
ptotal = 1
expsales = 0.0
exprest = 0.0
maxexpprofit = 0.0

for q in range(N + 1):
  p = float(input())
  exprest += (1 - ptotal)
  ptotal -= p
  expsales += q * p
  expprofit = r * (expsales + q * ptotal) - c * q + s * exprest
  if expprofit > maxexpprofit:
    maxexpprofit = expprofit
    optimalq = q
    
print(optimalq, int(maxexpprofit))


# 1 21
# 4 92
# 6 100
# 8 37
# 52 52