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

#ques 3:extract mont from time

import datetime
d=datetime.date.today()
print(d.month)