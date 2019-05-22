"""
Dhruv Jain
XII-D
Question 16
"""

shift = int(input("Enter shift value: "))
key = {}
x = input("Encode(e)/Decode(d)? ").lower()
inp = open("input.txt", "r")
out = open("output.txt", "w")

if x == "e":
    for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a = ord(i) + shift
        if a > ord("z"):
            a = ord(i) + shift - 26
        elif a > ord("Z") and i.isupper():
            a = ord(i) + shift - 26
        key[i] = chr(a)
    
    for i in inp.readlines():
        for j in i:
            if j.isalpha():
                out.write(key[j])
            elif j.isspace():
                out.write(" ")
            else:
                pass
        out.write("\n")
        
if x == "d":
    for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a = ord(i) - shift
        if a > ord("z"):
            a = ord(i) - shift + 26
        elif a > ord("Z") and i.isupper():
            a = ord(i) - shift + 26
        key[i] = chr(a)
        
    for i in inp.readlines():
        for j in i:
            if j.isalpha():
                out.write(key[j])
            elif j.isspace():
                out.write(" ")
            else:
                pass
        out.write("\n")

inp.close()
out.close()