#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

import tkinter
from tkinter import *
import sys

dic={"rahul":95943053548,"mohit":84593745722,"malay":94524592345,"rajan":87654322678,"nihal":7564565503,"rahul":856453545343,"satyam":8435340034554,"rajan":9845384754,"gurdeep":94954378758,"aman":83458439877,"nikhil":6345666764,"mukesh":85422422455,"deepak":84735822}

def insert():
	dic[entry1.get()]=int(entry2.get())
	l.insert(END, '{}: {}'.format(entry1.get(), entry2.get()))
	print(dic)
	
root=Tk()
root.title("window")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
root.maxsize(300,300)
root.configure(background="Beige")

entry1=Entry(root,width=20)
entry1.pack()

entry2=Entry(root,width=20)
entry2.pack()

b=Button(root,text='submit',width=5,command=insert)
b.pack()

f=Frame()
f.pack(side=LEFT)

s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
l=Listbox(f,yscrollcommand=s.set)

for key in dic:
    l.insert(END, '{}: {}'.format(key, dic[key]))
	
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())

root.mainloop()