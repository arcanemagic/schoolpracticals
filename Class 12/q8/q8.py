"""
Dhruv Jain
XII-D
Question 8
"""

import copy

l1 = [int(x) for x in input("Enter number: ").split(",") if x.isdigit()]
l2 = [int(x) for x in input("Enter number: ").split(",") if x.isdigit()]

def merge(l1,l2):
    l3 = copy.deepcopy(l1)
    for i in l2:
        if i not in l1:
            l3.append(i)
    return l3

def commonSum(l1,l2):
    sum = 0
    for i in l1:
        if i in l2:
            sum += i
    return sum

def isCircular(l1, l2):
    l3, l4 = "", ""
    l1.extend(l1)
    for i in l1:
        l3 += str(i)
    for i in l2:
        l4 += str(i)
    if l4 in l3 or l4[::-1] in l3:
        return True
    else:
        return False

print("Merged list:", merge(l1,l2))
print("Sum of common elements:", commonSum(l1,l2))
print("Circularly identical:", isCircular(l1,l2))
