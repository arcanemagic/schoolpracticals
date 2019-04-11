"""
Dhruv Jain
XI-D
Question 13
"""


isbn = int(input("Enter ISBN number: "))

check = isbn%10

sum = 0
for i in range(10, 0, -1):
    sum += (((isbn%(10**i) - isbn%(10**(i-1)))/(10**(i-1)))*((10-i)+1))

sum -= check*10

if(int(sum)%11 == check):
    print("ISBN is valid")
else:
    print("Invalid ISBN")
