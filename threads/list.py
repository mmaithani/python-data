#Q3. Make a list that has 5 elements.Create a threading 
#process that prints the 5 elements of the list with a 
#delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec

import threading
from threading import Thread
import time
l=[1,2,3,4,5]
def disp_list():
	print("delay of multiple of 2 sec is given below=")
	time.sleep(2)
	b=2
	for x in l:                                    #making a loop to print index values of list 
		print (x)                                 #printing list number:
		time.sleep(b)
		b=b+2                                      #extending sleep time here by 2 sec
m=Thread(target=disp_list)
m.start()

