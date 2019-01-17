"""
Dhruv Jain
XI-D
Question 3
"""

l = eval(input("Enter numbers in  list "))
d = {}

for i in l:
    d[i] = l.count(i)
for i in d:
    print(i, '\t', '*' * d[i])