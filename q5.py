"""
Dhruv Jain
XI-D
Question 5
"""

m = int(input("Enter amount of money in Rupees: "))
t = int(m/1000)
m = m%1000
f = int(m/500)
m = m%500
h = int(m/100)
m = m%100
fif = int(m/50)
m = m%50
ten = int(m/10)
m = m%10
five = int(m/5)
m = m%5
two = int(m/2)
m = m%2

print("\n You have", "\n", t, "Rs. 1000 notes,", "\n", f, "Rs. 500 notes,", "\n", h, "Rs. 100 notes,", "\n", fif, "Rs. 50 notes,", "\n", ten, "Rs. 10 notes/coins,", "\n", five, "Rs. 5 coins,", "\n", two, "Rs. 2 coins,", "\n", m, "Rs. 1 coins.")
