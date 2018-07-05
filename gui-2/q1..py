# Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter
# and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *
dict={'malay':9802515252,'manlay':98025152542,'mealay':98025165252,'malafy':98025515252,'malvay':98025152522,'malafy':98025152552,'maalay':98025152552,'mohit':9068161883,'sumit':9034314752}

# prinkey():


m=Tk()
m.title('malay')
m.geometry("200x200")
s=Scrollbar(m)
s.pack(side=RIGHT,fill=Y)
l=Listbox(m,yscrollcommand=s.set)
for key in dict:
    l.insert(END, key)
l.pack()
m.mainloop()