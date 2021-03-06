"""
Dhruv Jain
XII-D
Question 12
"""

f = open("text.txt", "w")
f.write("Neither apple nor pine are in pineapple. Boxing rings are square.\nWriters write, but fingers don't fing. Overlook and oversee are opposites.\nA house can burn up as it burns down. An alarm goes off by going on.\n")
f.close()

f = open("text.txt", "a+")
f.seek(0)
print(f.read())
f.write("People in Poland are called Poles but people in Holland are not called Holes.\n")
f.seek(0)
lineno = 1
for i in f:
    print(lineno,":",i)
    lineno += 1

f.seek(0)
print("Last line:",f.readlines()[-1])

f.seek(9)
print(f.readline())

lineno = int(input("Enter line number: "))
f.seek(0)
print(f.readlines()[lineno-1])

d = {}
f.seek(0)
for i in f.readlines():
    for j in i.split():
        j = j.lower()
        if j[0] not in d:
            d[j[0]] = 1
        else:
            d[j[0]] += 1

for i in d.items():
    print("Words beginning with",i[0],":",i[1])
