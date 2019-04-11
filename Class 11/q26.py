"""
Dhruv Jain
XI-D
Question 26
"""

import copy
n = int(input("Enter number to start: "))
l=[n]
while n != 1:
    if n%2 == 0:
        n=n//2
        l.append(n)
    else:
        n = (n*3)+1
        l.append(n)
print(l)

print("Length:", len(l))

lbub = copy.deepcopy(l)
bub = 0
for i in range(0,len(lbub)):
    for j in range(0,len(lbub)-i-1):
        if lbub[j]>lbub[j+1]:
            lbub[j],lbub[j+1]=lbub[j+1],lbub[j]
            bub+=1
print("Bubble Sorted: ", lbub)
print("Bubble Sorting Efficiency: ", bub)

lins = copy.deepcopy(l)
ins = 0
for i in range(1,len(lins)):
    a=lins[i]
    j=i-1
    while (a<lins[j]) and j>-1:
        lins[j+1]=lins[j]
        j=j-1
        ins+=1
    lins[j+1]=a
print("Insertion Sorted: ", lins)
print("Insertion Sorting Efficiency: ", ins) 
