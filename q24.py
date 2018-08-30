# -*- coding: utf-8 -*-
"""
Dhruv Jain
XI-D
Question 24
"""

s = input("Enter string: ")
a = input("Encrypt/Decrypt?: ")
try:
    b = int(input("Enter rotation number: "))
except:
    b = 13
c = ""

if a.lower() == "d":
    b = -1*b
for i in range(len(s)):
    if s[i].isspace() == False:
        d = ord(s[i])+b
        if d>ord("z"):
            d=(d-ord('Z'))%26 +ord('A')-1
        elif d<ord('A'):
            d=-1*((-d+ord('A'))%26) +ord('Z')+1
        c+=chr(d)
    else:
        c+=' '
print(c)
