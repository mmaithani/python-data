# Q.3- What will be the output of the following code:

# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not

#above will give error on name error




#here is the solution
try:
    raise NameError("Hi there")  # Raise Error
except Exception:
    print ("An exception")
      #  To determine whether the exception was raised or not
