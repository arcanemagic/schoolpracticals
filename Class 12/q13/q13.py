"""
Dhruv Jain
XII-D
Question 2
"""

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w+")
def isvowel():
    for i in f1.readlines():
        for j in i.split():
            if j[0] not in "aeiouAEIOU":
                f2.write(j+" ")
isvowel()
f1.seek(0)
f2.seek(0)
print("Original file:",f1.read())
print("New file:",f2.read())
f1.close()
f2.close()

