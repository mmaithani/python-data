#ques.1: what is time tuple
#A Python program can handle date and time in several ways. Converting between date formats is a common chore for computers. Python's time and calendar modules help track dates and times.
#Time intervals are floating-point numbers in units of seconds. Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).
#There is a popular time module available in Python which provides functions for working with times, and for converting between representations. The function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).

# import time;  # This is required to include time module.
#
# ticks = time.time()
# print("Number of ticks since 12:00am, January 1, 1970:", ticks)

#ques 2: WAP to get formatted time

#import time
#print(time.asctime())

#ques 3:extract month from time

import datetime
from datetime import date
d=date.today()
print(d.month)

#ques 4: extract day from time

#import datetime
#print(datetime.date.today().day)

#ques.5: Extract date (ex : 11 in 11/01/2021) from the time.

#import datetime
#t=datetime.date.today()
#print (t.day)

#ques.6: extract time using local time

#import datetime 
#import time
#print(time.localtime())
#print(datetime.datetime.time(datetime.datetime.now()))

#ques.7: find faCTORIAL

#import math
#s=int(input("enter number"))
#print(math.factorial(s))

#ques.8: find the gcd of number

#import math
#m=int(input("enter first number"))
#n=int(input("enter 2nd"))
#print(math.gcd(m,n))

#ques.9: use os mudule

#import os
#print(os.name)


















