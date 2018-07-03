# Q3. Create a frame using tkinter with any label text and two
#  buttons.One to exit and other
# to change the label to some other text.

import tkinter
import sys
from tkinter import *
root=Tk()
x=0
frame=Frame(root)
frame.pack()

t = IntVar()
t.set(0)
def click():

	if(t.get()==0):
		label.config(text="you are buffalo")
		t.set(1)
	else:
		label.config(text="you are awesome")
		t.set(0)
	

label=Label(root,text="hello ")
label.pack()

f1=Frame(root)
f1.pack(side=TOP)
# button.pack()

f2=Frame(root)
f2.pack(side=BOTTOM)


click_button=Button(f1,text='click! to change',command=click)
click_button.pack()

exit_button=Button(f2,text='Exit!',bg='powder blue',fg='black',command=sys.exit)
exit_button.pack()

root.mainloop()