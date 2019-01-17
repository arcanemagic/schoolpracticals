"""
Dhruv Jain
XI-D
Question 34
"""

d = {}

for i in range(1,7):
    for j in range(1,7):
        if (i+j) not in d:
            d[i+j] = ((i,j),)
        else:
            d[i+j] += ((i,j),)

print(d)