"""
Dhruv Jain
XII-D
Question 10
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("SI Calculator")
P = StringVar()
R = StringVar()
T = StringVar()
Label(root, text="Enter Principal Amount: ").grid(column=0, row=0)
Entry(root, width=20, textvariable=P).grid(column=2, row=0)
Label(root, text="Enter Rate of Investment: ").grid(column=0, row=1)
Entry(root, width=20, textvariable=R).grid(column=2, row=1)
Label(root, text="Enter Time Period: ").grid(column=0, row=2)
Entry(root, width=20, textvariable=T).grid(column=2, row=2)

def clicked():
    p = int(P.get())
    r = int(R.get())
    t = int(T.get())
    si = (p*r*t)/100
    messagebox.showinfo("Simple Interest", "Your interest is: "+str(si))
Button(root, text="Calculate Interest", command=clicked).grid(column=0, row=4)
Button(root, text="I am not interested", command=root.destroy).grid(column=2, row=4)

root.mainloop()