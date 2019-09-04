"""
Dhruv Jain
XII-D
Question 17
"""

import urllib

u = urllib.request.urlopen("https://www.pythonforbeginners.com")
f = open("downloaded.htm","w")

for i in u.readlines():
    print(i)
    f.write(str(i))
    
print("Headers:")
print(u.headers)

u.close()
f.close()