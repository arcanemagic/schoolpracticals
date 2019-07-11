"""
Dhruv Jain
XII-D
Question 5
"""

n = int(input("Enter number in decimals: "))
c = input("Choose B for binary, O for octal, H for hexadecimal: ").upper()

def toStr(n, base):
	convertString = "0123456789ABCDEF"
	if n < base:
		return convertString[n]
	else:
		return toStr(n//base, base) + convertString[n%base]

if c == "B": c= 2
if c == "O": c = 8
if c == "H": c = 16

print(toStr(n,c))
