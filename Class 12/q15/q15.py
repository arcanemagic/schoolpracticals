"""
Dhruv Jain
XII-D
Question 15
"""

f = open("myfile.txt", "r")
d = {}
words = 0

for i in f.readlines():
    for j in i.split():
        if j.lower() in d:
            d[j.lower()] += 1
        else:
            d[j.lower()] = 1
            
for i in d.values():
    words += i
print("Total number of words:", words)
print("Number of different words:", len(d.keys()))
maxword, maxcnt = "", 0
for i in d.items():
    if i[1] > maxcnt:
        maxcnt = i[1]
        maxword = [i[0]]
    elif i[1] == maxcnt:
        maxword.append(i[0])
print("Most common word(s) is/are:", maxword)
    
d1 = {}
for i in d:
    if len(i) in d1:
        d1[len(i)].append(i)
    else:
        d1[len(i)] = [i]
        
def find_longest_word():
    return d1[max(d1)]

print("Longest word(s) is/are:",find_longest_word())

l2 = []
def filter_long_words(n):
    print("Words longer than", n, "are:")
    for i in d1:
        if i > n:
            l2.extend(d1[i])
            print(d1[i])

filter_long_words(8)

f.seek(0)
l = f.read().lower().split()
f1  = open("newfile.txt","w")
for i in l:
    if i not in l2:
        f1.write(i)
        f1.write(" ")
f1.close()
