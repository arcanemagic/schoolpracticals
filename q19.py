"""
Dhruv Jain
XI-D
Question 19
"""

d = str(input("Enter day: "))
m = int(input("Enter month: "))
y = str(input("Enter year: "))

mon = {1:"JAN", 2:"FEB", 3:"MAR", 4:"APR", 5:"MAY", 6:"JUN", 7:"JUL", 8:"AUG", 9:"SEP", 10:"OCT", 11:"NOV", 12:"DEC"}

print(d + "-" + mon[m] + "-" + y[-2] + y[-1])