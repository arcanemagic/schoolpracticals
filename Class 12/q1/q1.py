"""
Dhruv Jain
XII-D
Question 1
"""

password = input("Enter password: ").split(",")
lower, upper, number, special = 0, 0, 0, 0

for j in password:
    for i in j:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            number += 1
        elif i in "@#$":
            special += 1
    if lower > 0 and upper > 0 and number > 0 and special > 0:
        print("Valid password is", j)
        break
    else:
        lower, upper, number, special = 0, 0, 0, 0
