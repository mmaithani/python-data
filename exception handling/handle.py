# Q.1- Name and handle the exception occured in the following program: 
try:
 a=3
 if a<4:
     a=a/(a-3)
     print(a)
except Exception as e:
	print(e)
