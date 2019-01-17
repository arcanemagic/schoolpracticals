"""
Dhruv Jain
XI-D
Question 28
"""

l = eval(input("Enter list: "))
op = 0

for i in range(1,len(l)):
    a = l[i]
    j = i-1
    while (a < l[j]) and j > -1:
        l[j+1] = l[j]
        j = j-1
        op += 1
    l[j+1] = a

print("Sorted list: ", l)
print("Number of operations: ", op)