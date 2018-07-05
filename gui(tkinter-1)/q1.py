# Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import sys
import tkinter

from tkinter import *
root=Tk()
def show():
    print("Hello World")

def end():
    sys.exit()
b1=Button(root,text="hello world",width=20,command=show)
b1.pack()

b2=Button(root,text="click!",width=25,command=end)
b2.pack()
root.mainloop()