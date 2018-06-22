#Q4. Call factorial function using thread.
import threading
from threading import Thread
import time
def fact(g):
	x=1
	print("Factorial of number >",g,"is")
	for i in range(1,g+1):
		x=x*(g)
		g=g-1
	print(x) 
	               #x=1*1  2*5 3*5
g=int(input("enter the number you want factorial=>"))
t=Thread(target=fact,args=(g,))
t.start()	