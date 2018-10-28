"""
Dhruv Jain
XI-D
Question 7
"""

l = int(input("Enter no. of legs: "))
h = int(input("Enter no. of heads: "))

r = int((l-2*h)/2)
c = int(h-r)

print("\n Number of rabbits is", r, "\n Number of chickens is", c)
