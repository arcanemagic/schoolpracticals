"""
Dhruv Jain
XII-D
Question 14
"""

f = open("data.txt", "r")
l = f.readlines()
for i in range(len(l)):
    l[i] = tuple(l[i].split())

def sortNew(n):
    return n[2]
l.sort(key = sortNew)

d = {}
print("People with Experience less than 3 years:")
for i in l:
    if int(i[3]) < 3:
        print(i[0], i[1])
    if i[4] in d:
        d[i[4]] += 1
    else:
        d[i[4]] = 1
print()
for i in d.items():
    print(i[0],":",i[1])