"""
Dhruv Jain
XI-D
Question 10
"""

n = int(input("Enter number: "))
a = 1
m = n
cnt = 0
while(m>0):
    cnt = cnt+1
    m = m//10
sum = 0
prod = 1

if cnt%2 == 0:
    while(n%(10**(a-1)) != n):
        if(a%2 == 0):
            sum = sum+((n%(10**a))-(n%(10**(a-1))))/(10**(a-1))
        else:
            prod = prod*((n%(10**a))-(n%(10**(a-1))))/(10**(a-1))
        a = a+1
else:
    while(n%(10**(a-1)) != n):
        if(a%2 == 0):
            prod = prod*((n%(10**a))-(n%(10**(a-1))))/(10**(a-1))
        else:
            sum = sum+((n%(10**a))-(n%(10**(a-1))))/(10**(a-1))
        a = a+1

print("Sum of odd positioned digits:", int(sum), "\nProduct of even positioned digits:", int(prod),
      "\nSum of above two results:", int(sum+prod))
