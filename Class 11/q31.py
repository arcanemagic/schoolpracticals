"""
Dhruv Jain
XI-D
Question 31
"""

l = input("Enter sentence: ").split()
d = {}

for i in l:
    if not(i in d):
        d[i] = l.count(i)
        
print(d)
