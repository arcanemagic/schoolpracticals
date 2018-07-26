# -*- coding: utf-8 -*-
"""
Dhruv Jain
XI-D
"""

n = int(input("Enter number of rows: "))

num = ord("A")

for i in range(n):
   print((n-i-1)*" ", end=" ")
   for j in range(i+1):
       print(chr(num), end=" ")
       num = num +1
       if num == 91:
           num = 65
   print("\r")