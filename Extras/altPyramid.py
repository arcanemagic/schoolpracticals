# -*- coding: utf-8 -*-
"""
Dhruv Jain
XI-D
"""

n = int(input("Enter number of lines: "))
cnt = ord("Z")
for i in range(1, n+1):
    if i%2 == 0:
        print("\n", "#"*i)
    else:
        for j in range(i):
            print(chr(cnt), end=" ")
            cnt = cnt-1
            if cnt<ord("A"):
                cnt = ord("Z")