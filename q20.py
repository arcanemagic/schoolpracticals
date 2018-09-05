"""
Dhruv Jain
XI-D
Question 20
"""

import math

t = int(input("Enter number of rows: "))

def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascals_triangle(rows):
    result = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result
i=0
for row in pascals_triangle(t):
    print(" "*((t*2)-i), end="")
    i += 2
    for x in row:
        print(str(x), end="   ")
    print("")