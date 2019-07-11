"""
Dhruv Jain
XII-D
Question 5
"""

n = int(input("Enter number in decimals: "))
r = 0
num = ""
c = input("Choose B for binary, O for octal, H for hexadecimal: ").upper()
if n == 0:
    num = "0"
if c == "B":
    while n!=0:
        r = n%2
        num += str(r)
        n = n//2

elif c == "O":
    while n!=0:
        r = n%8
        num += str(r)
        n = n//8

elif c == "H":
    while n!=0:
        r = n%16
        if r>9:
            r = chr(ord("A")+r-10)
        num += str(r)
        n = n//16
else:
    print("Number system not recognized!")
print(num[::-1])
