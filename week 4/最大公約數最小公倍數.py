# week4/最大公約數最小公倍數.py

# define a function
def compute_hcf(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

print("Give 2 numbers and we give you their Highest Common Factor.")
x = input("Give give a positive integer: ")
y = input("Give another positive integer: ")
x = int(x)
y = int(y)
print(f"The Highest Common Factor is: {compute_hcf(x, y)}")

z = x * y / compute_hcf(x, y)

print("The Least Common Multiple is: {:.0f}".format(z))