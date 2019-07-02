"""
Dhruv Jain
XII-D
Question 2
"""

n = input("Enter number: ")

def count(n):
    return len(n)

def reverse(n):
    return n[::-1]

def hasdigit(n):
    a = input("Enter digit to check: ")
    return a in n

def show(n):
    n = int(n)
    result = []
    divider = 10
    while divider < n:
        temp = n % divider
        if temp != 0:
            result.insert(0, str(temp))
        n -= temp
        divider *= 10
    result.insert(0, str(n))
    return '+'.join(result)
