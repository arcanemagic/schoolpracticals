"""
Dhruv Jain
XI-D
Question 6
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
o = str(input("Choose an operator + - * /: "))

if o == "+":
    c = a+b
elif o == "-":
    c = a-b
elif o == "*":
    c = a*b
elif o == "/":
    c = a/b
else:
    c = str("unknown operator")

print("Your answer is", c)
