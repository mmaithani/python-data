#classes and modules-2

#another assignment on object and classes
class A:
	def show(self):
		print("class a")
class B(A):
	def show(self):
		print("class b")
def display(obj):
	obj.show()
a=A()
b=B()
display(a)
display(b)	
# class c(a,b):
#  	def show(self):
#  		print("class c")
# C=c()
# C.show()
# C.show()
# C.show()
