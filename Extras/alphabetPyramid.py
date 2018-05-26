# -*- coding: utf-8 -*-
"""
Created on Sat May 26 00:25:50 2018

@author: Dhruv Jain
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