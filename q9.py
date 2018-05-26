"""
Dhruv Jain
XI-D
Question 9
"""

u = int(input("Enter consumed units: "))

if u<=100:
    p = (40*u)/100
elif u<=300:
    p = ((40*100)+(50*(u-100)))/100
else:
    p = ((40*100)+(50*200)+(60*(u-300)))/100

print("Your final charge is Rs.", p+50)
