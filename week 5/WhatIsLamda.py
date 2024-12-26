# week 5/WhatIsLamda.py



# lambda paramenter1, parameter2,:expression

# function as an example
# function name is square


def square(num):
    value = num ** 2
    return value

# call the function for parameter 4, return value

print(square(4))  # print the content of function square with paramenter 4

# change to lambda function format
#  将函数名作为函数结果返回

x = lambda num:num**2
print(x(4))

