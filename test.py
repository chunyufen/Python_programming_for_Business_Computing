print(0.1 + 0.2 == 0.3) # will give false because decimal figures are represented as binaries and are never exact amounts. therefore use "round" to judge float.

print(round( 0.1 + 0.2, 1) == 3) # will give true because round(a, b) means apply 4 delete and become 5 to a, with b decimal places.

print(round( 0.1 + 0.2, 1))
