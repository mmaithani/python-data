#Q2. Make a thread that prints numbers from 1-10, 
#waits for 1 sec between
import threading
from threading import Thread
import time
def prin():
	
	for i in range(1,11):
		time.sleep(1/2)
		print(i)
		
		
t=Thread(target=prin)
t.start()


