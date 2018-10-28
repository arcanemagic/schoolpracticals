# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:44:47 2018

@author: Dhruv Jain
"""

l = eval(input("Enter list to sort: "))
print("List before sorting:", l)
for i in range(1, len(l)):
    key = l[i]
    j = i-1
    while j>-1 and key<l[j]:
        l[j+1] = l[j]
        j = j-1
    else:
        l[j+1] = key
print("Sorted list:", l)