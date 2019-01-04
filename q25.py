"""
Dhruv Jain
XI-D
Question 25
"""

n = int(input("Enter number of numbers: "))
l = []
f = []

for i in range(n):
    l.append(int(input("Enter number: ")))
for i in l:
    if i not in f:
        f.append(i)
        print(i,":", l.count(i)*"*")
