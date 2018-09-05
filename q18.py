"""
Dhruv Jain
XI-D
Question 18
"""

n = int(input("Enter number of terms: "))
x = float(input("Enter x: "))
s1, s2 = 0, 0

for i in range(1, n+1):
    s1 += (x**i)/i
    s2 += i/((i+1)**(1/2))
    
print("Sum of series A:", s1, "\nSum of series B:", s2)