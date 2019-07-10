"""
Dhruv Jain
XII-D
Question 6
"""

import matplotlib.pyplot as plt
states = ["Uttar Pradesh", "Madhya Pradesh", "Maharashtra", "Rajasthan", "Assam", "Karnataka", "Haryana", "West Bengal", "Tamil Nadu", "Arunachal Pradesh"]
pop = [820, 240, 370, 200, 397, 320, 573, 1029, 550, 17]
plt.pie(pop, labels=states)
plt.show()