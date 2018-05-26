"""
Dhruv Jain
XI-D
Question 8
"""

spd = int(input("Enter speed: "))
bd = input("Is today your birthday? ")

if bd.lower()=="yes":
    if spd<=65:
        t = str("no ticket")
    elif spd<=85:
        t = str("a small ticket")
    else:
        t = str("a big ticket")

elif bd.lower()=="no":
    if spd<=60:
        t = str("no ticket")
    elif spd<=80:
        t = str("a small ticket")
    else:
        t = str("a big ticket")

print("You have recieved", t)
