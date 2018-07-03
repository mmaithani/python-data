#now it will print on gui display
import sys
import tkinter
from tkinter import *
root=Tk()
def click():
    w=Label(root, text="ok hi there")
    w.pack()
b1=Button(root,text="hello world",width=20,command=click)
b1.pack()

root.mainloop()