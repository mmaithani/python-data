# Q.5- Write a program to show and handle following exceptions: 
# 1. Import Error
# 2. Value Error
# 3. Index Error

#3. Index error
try:
	l=[1,2,5,6]
	print(l[10])
except Exception as e:
	print(e)

#1. import error

try:
	from sumit import mohit
except Exception as m:
	print(m)	


try:
	import programs.my_python_program
	programs.my_python_program.main()	
except Exception as x:
	print (x)	

#2. value error

try:
	x=int("dfkb")
	print(x)
except Exception as k:
	print(k)
