# week 2/转换温度3.py

"""評估函數 eval()：去掉參數最外側引號並執行餘下語句的函數
eval()函數的基本使用格式：eval(<字串或字串變數>)
eval("1") = 1
eval("1+2") = 3
eval('"1+2"') = '1+2'
eval('print("Hello")') = Hello
eval(TempStr[0:-1] = 45 (float), if TempStr = 45F (str)
don't use var() even suggested by lecturer
see https://www.udacity.com/blog/2023/03/pythons-eval-the-most-powerful-function-you-should-never-use.html
Python's eval(): the most powerful function you should never use.
"""

TempStr = input("請輸入帶有符號的溫度值：")  # The output is a string
if TempStr[-1] in ['F', 'f']:  # ['F', 'f'] is a list
    C = (eval(TempStr[0:-1]) - 32)/1.8 # change string to float for calculation by function eval, which removes the most outside quotation marks and carry on the instruction (see explanation below)
    print("轉換後的溫度是{:.2f}C".format(C)) # {:} is fill in the blank, with what? with C, in what format? with 2 decimal places (.2f) 
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("轉換後的溫度是{:.2f}F".format(F))
else:
    print("輸入格式錯誤。")
    

