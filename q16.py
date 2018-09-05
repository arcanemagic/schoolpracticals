"""
Dhruv Jain
XI-D
Question 16
"""

print("y  ", "x    ", "i ")
print("-  ", "---  ", "----")

for i in range(1, 7):
    y = i
    x = 5.5 + (0.5*i)
    i = 2*(y - (0.5*x))
    print(y, " ", x, " ", i, " ")