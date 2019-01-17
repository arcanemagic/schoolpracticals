"""
Dhruv Jain
XI-D
Question 27
"""

l = eval(input("Enter list of numbers: "))
op = 0

for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            op += 1
            
print("Sorted list: ", l)
print("Number of operations: ", op)