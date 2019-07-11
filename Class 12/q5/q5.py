"""
Dhruv Jain
XII-D
Question 5
"""

n = int(input("Enter number in decimals: "))
c = input("Choose B for binary, O for octal, H for hexadecimal: ").upper()

def binary(n):
    if n < 2:
        return str(n)
    else:
        return str(n%2) + binary(n//2)

def octal(n):
    if n < 8:
        return str(n)
    else:
        return str(n%8) + octal(n//8)

def hex(n):
    if n < 16:
        if n > 9:
            n = chr(ord("A")+n-10)
        return str(n)
    else:
        a = n%16
        if a>9:
            a = chr(ord("A")+a-10)
        return str(a) + hex(n//16)

if c == "B":
    print(binary(n)[::-1])

elif c == "O":
    print(octal(n)[::-1])

elif c == "H":
    print(hex(n)[::-1])

else:
    print("Number system not recognized!")
