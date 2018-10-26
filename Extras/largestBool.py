# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:17:01 2018

@author: amity
"""

n=int(input("Enter number of numbers: "))
l=[]
x=""
for i in range(n):
    x=input("Enter 4 digit binary number: ")
    l.append(x)
l.sort()
print(l[n-1])
m=list(l[n-1])
s=((2**3)*int(m[0]))+((2**2)*int(m[1]))+(2*int(m[2]))+int(m[3])
print(s)