"""
Dhruv Jain
XI-D
Question 12
"""

n=int(input("Enter number of students "))
a=b=c=d=0
for i in range (n):
    age=int(input("Enter Age in years "))
    if age<12:
        d+=1
    elif age<15:
        a+=1
    elif age<17:
        b+=1
    elif age<19:
        c=+1
print("\n Group A:",a,"\n Group B:",b,"\n Group C:",c,"\n Group D:",d)

