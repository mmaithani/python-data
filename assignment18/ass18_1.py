#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar 
#to scroll the list of keys in the dictionary.

import tkinter
from tkinter import *
import sys

dic={"rahul":95943053548,"mohit":84593745722,"malay":94524592345,"rajan":87654322678,"nihal":7564565503,"rahul":856453545343,"satyam":8435340034554,"rajan":9845384754,"gurdeep":94954378758,"aman":83458439877,"nikhil":6345666764,"mukesh":85422422455,"deepak":84735822}

root=Tk()
root.title("window")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
root.maxsize(300,300)
root.configure(background="Beige")

f=Frame()
f.pack(side=LEFT)
label=Label(f,text="MY LIST")
label.pack()

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set)
for x in dic:
	l.insert(END,x)
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())

root.mainloop()
