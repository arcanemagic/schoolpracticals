"""
Dhruv Jain
XII-D
Question 19
"""

class queue:
    def __init__(self):
        self.q = []
    def enqueue(self, admissionEntry):
        self.q.append(admissionEntry)
    def length(self):
        return len(self.q)
    def applicationByClass(self):
        nur, kg, one = 0, 0, 0
        for i in self.q:
            if i[2] == "Nursery":
                nur += 1
            elif i[2] == "KG":
                kg += 1
            else:
                one += 1
        print("Number of applications for Nursery:", nur)
        print("Number of applications for KG:", kg)
        print("Number of applications for Class I:", one)

adm = []
q = queue()
i = 1
n = int(input("Enter number of entries: "))

class incorrectDataEntry(Exception):
    pass

while i <= n:
    try:
        l1 = input("Enter registration no: ")
        l2 = input("Enter name: ")
        l3 = input("Enter class of admission (Nursery/KG/I): ")
        if l3 != "Nursery" and l3 != "KG" and l3 != "I":
            raise incorrectDataEntry
    except:
        print("Data entry incorrect, try again!")
        continue
    
    q.enqueue([l1, l2, l3])
    print(q.q)
    i += 1

print("Length of queue:", q.length())
q.applicationByClass()