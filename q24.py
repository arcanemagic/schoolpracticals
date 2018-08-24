# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:50:01 2018

@author: amity
"""

s = input("Enter string to encrypt/decrypt: ")
c = input("Encrypt(E)/Decrypt(D)? ")
n = int(input("Enter rotation number: "))
x = ""
if c.lower() == "e":
    for i in range(len(s)):
        if s[i].isspace():
            x+= " "
            continue
        if (ord(s[i])+n) > ord("z"):
            x += chr(((ord(s[i])+n)-ord("z"))%26 + ord("a")-1)
        else:
            x += chr(ord(s[i])+n)
elif c.lower() == "d":
    for i in range(len(s)):
        if s[i].isspace():
            x+= " "
            continue
        if (ord(s[i])-n) < ord("a"):
            x += chr((ord("z"))+((ord("a")-ord(s[i])-n))+3)
        else:
            x += chr(ord(s[i])-n)
print(x)