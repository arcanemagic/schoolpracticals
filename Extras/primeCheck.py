# -*- coding: utf-8 -*-
"""
Dhruv Jain
XI-D
"""

n = int(input("Enter number to check: "))

for i in range(2, int(n**(1/2)+1)):
    if n%i == 0:
        print("Not a prime")
        break
else:
    print("Number entered is prime")