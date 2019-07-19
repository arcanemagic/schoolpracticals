"""
Dhruv Jain
XII-D
Question 9
"""

import numpy as np

a = np.random.randint(10, size=(5,5))
max = 0

print(a)
print("Maximum value:", np.max(a))
print("Minimum value:", np.min(a))

for i in a:
    if np.bincount(i).argmax()>max:
        max = np.bincount(i).argmax()

value = int(input("Enter scalar value: "))
def closestToScalar(array, value):
    i = np.abs(array - value).argmin()
    return a.flat[i]
        
print("Most frequently occuring:", max)
print("Closest value to scalar in array:", closestToScalar(a, value))