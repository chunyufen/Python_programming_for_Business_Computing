# Week-4/SingleProductPricing.py

a = int(input("base demand = "))
b = int(input("price sensitivity = "))
c = int(input("unit cost = "))

max_profit = 0
optimal_price = 0
for p in range(c + 1, a // b):
    profit = (a - b * p) * (p - c)
    # print(p, profit)
    
    if profit > max_profit:
        max_profit = profit
        optimal_price = p
    else:
        break
        
print("optimal price = " + str(optimal_price))
print("maximized profit = " + str(max_profit))