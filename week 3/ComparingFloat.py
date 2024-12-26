# week 3/ComparingFloat.py

"""This script demonstrates the comparison of floating-point numbers in Python, which can sometimes lead to unexpected results due to precision errors. It checks if the sum of 0.1 and 0.2 equals 0.3, which is known to be False due to floating-point arithmetic. The script also uses the round function to compare the sum rounded to one decimal place with 0.3, and prints the rounded result.
"""

print(0.1 + 0.2 == 0.3)
print(round( 0.1 + 0.2, 1) == 3)
print(round( 0.1 + 0.2, 1))