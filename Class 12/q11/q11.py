"""
Dhruv Jain
XII-D
Question 11
"""

l = [int(x) for x in input("Enter number: ").split(",") if x.isdigit()]
a = int(input("Enter element to find: "))

def bubbleSort(l):
    iter = 0
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
            iter += 1
    print("\nNo. of iterations for bubble sort:", iter)
    return l

def binarySearch(l, a):
    low, high, iter = 0, len(l)-1, 0
    while low <= high:
        iter += 1
        mid = (low + high)//2
        if l[mid] == a:
            print("\nNo. of iterations for binary search:", iter)
            return mid
        elif l[mid] < a:
            low = mid + 1
        else:
            high = mid - 1
    print("\nNo. of iterations for binary search:", iter)
    return -1

def linearSearch(l, a):
    iter = 0
    for i in range(len(l)):
        if l[i] == a:
            print("\nNo. of iterations for linear search:", iter)
            return i
        iter += 1
    print("\nNo. of iterations for linear search:", iter)
    return -1

print("Sorted list:", bubbleSort(l))
print("Index of element:", binarySearch(l, a))
print("Index of element:", linearSearch(l, a))
