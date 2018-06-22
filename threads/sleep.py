#Q1. Create a threading process such that 
#it sleeps for 5 seconds and then prints out a message.

import threading
from threading import Thread
import time
def disp():
	time.sleep(5)
	print("next message appear 5 second")
t=Thread(target=disp)
t.start()
