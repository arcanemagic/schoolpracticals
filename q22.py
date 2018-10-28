# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:45:48 2018

@author: amity
"""

s=input("Enter string: ")
for i in range(10000):
    if chr(i) in s:
        print(chr(i), "=", s.count(chr(i)),", ", end="")
print("\n")

maxLen=0
maxWord=""
currentWord=""
currentLen=0
isWord=False
for i in s:
    if i.isalpha():
        currentLen+=1
        currentWord+=i
        if not isWord:
            isWord=True
    else:
        if isWord:
            currentLen=0
            currentWord=""
        isWord=False
    if currentLen>maxLen:
        maxLen=currentLen
        maxWord=currentWord
print(maxWord)

s2 = " "+s
newS=""
for i in range(1,len(s2)):
    if s2[i-1].isspace() and s2[i].isalpha():
        newS += s2[i].upper()
    else:
        newS += s2[i]
print(newS)

name=input("Enter name: ")
name=" "+name
newS=""
for i in range(1,len(name)):
    if name[i-1].isspace() and name[i].isalpha():
        newS += name[i].upper()
        newS+=" "
print(newS)
