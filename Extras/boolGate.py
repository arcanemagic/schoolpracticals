# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:49:21 2018

@author: amity
"""

n=int(input("Enter number of inputs: "))
x=0
a=[None]*n
for i in range(n):
    x=int(input("Enter 1/0: "))
    if x==0:
        a[i]=False
    else:
        a[i]=True

gate=input("What gate do you want to use?")
if gate.lower() == "and":
    print(all(a))
elif gate.lower() == "or":
    print(any(a))
elif gate.lower() == "xor":
    out = a[0]
    for i in range(1,len(a)):
        out = int(out) ^ int(a[i])
    if out == 0:
        out = False
    else:
        out = True
    print(out)
elif gate.lower() == "nor":
    print(not(any(a)))
elif gate.lower() == "nand":
    print(not(all(a)))