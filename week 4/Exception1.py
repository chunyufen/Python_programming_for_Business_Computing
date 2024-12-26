# week 4/Exception1.py

# try块包含可能会引发异常的代码。如果在执行try块中的代码时发生异常，Python会停止当前的执行流程，并跳转到相应的except块来处理这个异常。

try:
    num = eval(input("请输入一个整数: "))
    print(num**2)
except NameError:
    print("输入错误，请输入一个整数!")