# Q4. Write a python program using tkinter interface to take an
# input in the GUI program and print it.

import tkinter
import sys
from tkinter import *
root=Tk()

l=Label(root,text="Enter")

e1=Entry(root)
e1.pack()
def show():
	print(e1.get())

button=Button(root,text='submit',command=show)
button.pack()

root.mainloop()