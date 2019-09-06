"""
Dhruv Jain
XII-D
Question 18
"""

class ringTower:
    def __init__(self, ringCondition = False):
        self.s = []
        self.ring = ringCondition

    def isEmpty(self):
        if self.s == []:
            return True
        else:
            return False

    def push(self, item, tempTower):
        if self.ring:
            while item < self.peek():
                tempTower.s.append(self.pop())
            else:
                self.s.append(item)
                while not tempTower.isEmpty():
                    self.s.append(tempTower.pop())
        else:
            self.s.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return(self.s.pop())
        else:
            return False

    def peek(self):
        if not self.isEmpty():
            return (self.s[-1])
        else:
            return 0

rings = ringTower(True)
temp = ringTower()

while True:
    try:
        rings.push(int(input("Enter number: ")), temp)
        print("Ring Tower:", rings.s)
    except:
        print("Done")
        break