"""
Dhruv Jain
XI-D
Question 32
"""

l = input("Enter sentence: ").split()
d = {}

for i in l:
    if l.count(i) not in d:
        d[l.count(i)] = [i]
    else:
        if i not in d[l.count(i)]:
            d[l.count(i)].append(i)
        
print(d)
