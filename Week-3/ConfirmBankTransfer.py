# Week-2/ConfirmBankTransfer.py
"""在兩個戶頭之間轉帳，是非常普通的一個金融交易。假設我們現在有兩個帳戶，戶頭金額各為 x_1和 x_2，而我們想要從第一個戶頭轉 y 元到第二個戶頭，則一般情況下兩個戶頭的金額各會變成 x_1 - y 和 x_2 + y。但如果第一個戶頭錢不夠的話，我們就把第一個戶頭的錢扣到變成 0，然後把第二個戶頭的錢變成 x_2 + x_1。舉例來說，如果原本兩個戶頭各有 1000 和 2000 元，而我們要轉 500 元，那就會變成 500 和 2500，但如果要轉 1000 元，就會變成 0 和 3000。

請寫一個程式，讀入 x_1, x_2 和 y 之後，判斷兩個戶頭各應該變成多少錢。
"""


transferee = float(input("Account balance of account 1: "))
transferor = float(input("Account balance of account 2: "))
transfer_sum = float(input("Amount to transfer from account 1 to account 2: "))
balance_transferee = transferee - transfer_sum
balance_transferor = transferor + transfer_sum
if balance_transferee >= 0:
    print("Account 1 balance: ", balance_transferee)
    print("Account 2 balance: ", balance_transferor)
else:
    balance_transferor = transferor + transferee
    balance_transferee = 0
    print("Account 1 balance: ", balance_transferee)
    print("Account 2 balance: ", balance_transferor)

# Account 1 balance:  95176.0
# Account 2 balance:  81187.0


# Account 1 balance:  0
# Account 2 balance:  99546.0

# Account 1 balance:  0.0
# Account 2 balance:  0.0

# Account 1 balance:  0.0
# Account 2 balance:  200000.0

# Account 1 balance:  12189.0
# Account 2 balance:  35178.0