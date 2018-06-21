#another assignment on object and classes
class a:
	def show(self):
		print("class a")
class b():
	def show2(self):
		print("class b")
class c(a,b):
 	def show3(self):
 		print("class c")
C=c()
C.show()
C.show2()
C.show3()
