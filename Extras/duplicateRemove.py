l=list(input("Enter elements: "))
x=input("Enter element to remove duplicates: ")
s=l.index(x)
l1=l[s+1::]
while x in l1:
    l1.remove(x)
l=l[:s+1:]+l1
print(l)