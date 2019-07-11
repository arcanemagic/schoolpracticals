"""
Dhruv Jain
XII-D
Question 4
"""

import math

n = int(input("Enter number of rows: "))

def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new = [1]
        result = triangle(n-1)
        prev = result[-1]
        for i in range(len(prev)-1):
            new.append(prev[i] + prev[i+1])
        new += [1]
        result.append(new)
    return result

for i in triangle(n):
    for j in i:
        print(j, end=" ")
    print()
