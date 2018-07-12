# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:26:32 2018

@author: amity
"""

n = int(input("Enter number to check: "))

for i in range(2, int(n**(1/2)+1)):
    if n%i == 0:
        print("Not a prime")
        break
else:
    print("Number entered is prime")