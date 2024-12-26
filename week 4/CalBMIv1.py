# week 4/CalBMIv1.py
"""This script calculates the Body Mass Index (BMI) based on user input for height and weight.
It categorizes the BMI into different health categories such as underweight, normal weight, overweight, and obese.
"""
height, weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]: "))  # 首先，代码通过input函数提示用户输入身高和体重，两者之间用逗号隔开。这里使用了eval函数来将用户输入的字符串转换为数值类型，这样就可以进行数学计算了。例如，用户输入1.75, 70，height将被赋值为1.75，weight将被赋值为70。
bmi = weight / pow(height, 2)  # 接下来，代码计算BMI值，公式是体重（公斤）除以身高（米）的平方。计算结果存储在变量bmi中。
print("BMI 数值为: {0}".format(bmi))
who = ""
if bmi < 18.5:  # 然后，代码使用一系列的if和elif语句来判断BMI值对应的体重状况。这些条件语句按照BMI值的范围来划分不同的体重状况，例如偏瘦、正常、偏胖和肥胖。注意这里有一个小错误，elif 24 <= bmi < 25:这个条件是多余的，因为它和elif 18.5 <= bmi < 24:的条件范围重叠了。
    who = "偏瘦"
elif 18.5 <= bmi < 24:
    who = "正常"
elif 24 <= bmi < 25:
    who = "正常"
elif 25 <= bmi < 28:
    who = "偏胖"
elif 28 <= bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"
print("BMI 指标为: {0}".format(who))  # 最后，代码使用print函数输出计算得到的BMI数值和对应的体重状况。

"""在这段代码中，需要注意的是使用eval函数可能会带来安全风险，因为它会执行传入的字符串作为代码，如果用户输入恶意代码，可能会导致程序崩溃或者数据泄露。在实际应用中，应该使用更安全的方法来处理用户输入，例如使用float函数来转换身高和体重的输入。
"""

