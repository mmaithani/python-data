# Q.4- What will be the output of the following code:

 # Function which returns a/b
# def AbyB(a , b):
# 	try:
# 		c = ((a+b) / (a-b))
# 	except ZeroDivisionError:
# 		print "a/b result in 0"
# 	else:
# 		print c

# # Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

#it will give syntax error in line 8


#here is the solution
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisisonError:
		print("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
