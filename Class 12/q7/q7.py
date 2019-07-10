"""
Dhruv Jain
XII-D
Question 7
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,11,0.1)
y1 = np.exp(-1*x/10)*np.sin(math.pi*x)
y2 = x*np.exp(-1*x/3)

plt.plot(x, y1, label="f(x)")
plt.plot(x, y2, label="g(x)")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("Graph.jpg")
plt.show()