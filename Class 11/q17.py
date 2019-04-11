"""
Dhruv Jain
XI-D
Question 17
"""

import random
a=random.randint(1,20)
c=0
print("(Only three chances allowed)")
name=input("Hello! What is your name? ")
print("Well",name,", I have chosen a number between 1 and 20.")

for i in range(0,3):
    g=int(input("Take a guess. "))
    c+=1
    if g==a:
        print('Good job',name,', you guessed my number in',c,'guesses!')
        break
    elif g<a:
        print('Your guess is too low')
    else:
        print('Your guess is too high')
