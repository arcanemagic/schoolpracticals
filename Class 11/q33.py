"""
Dhruv Jain
XI-D
Question 33
"""

d = {"rose":("red","black","pink","white"),"lily":("violet","white","red")}
a = ()

for i in d.values():
    a += i

maxcol = 0
maxcolour = ""

for i in a:
    if a.count(i) > maxcol:
        maxcol = a.count(i)
        maxcolour = i

print("Most colours available:", max(d.items())[0])
print("Most flowers available:", maxcolour)
