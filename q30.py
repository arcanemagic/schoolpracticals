"""
Dhruv Jain
XI-D
Question 30
"""

d = {}
relatives = {"Lisa":"daughter","Bart":"son","Marge":"mother","Homer":"father","Santa":"dog"}
ages={"Lisa":8,"Bart":10,"Marge":35,"Homer":40,"Santa":2}

for i in relatives:
    d[i]=([relatives[i],ages[i]])

print("The Simpsons")

for j in d:
    print(j,"is a",d[j][0],"and is",d[j][1],"years old")