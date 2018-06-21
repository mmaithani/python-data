# Q.4- Create a class Shape.Initialize it with length and 
# breadth Create the method Area. Create class 
# rectangle and square which inherits shape and access the method Area.

class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
         self.areaa=self.length*self.breadth
         print("area=>",self.areaa)

class rectangle(shape):
    def Area(self):
        print("rectanle area=>")
        super().Area()

class square(shape):
    def Area(self):
        print("square")
        super().Area()


leng = int(input("enter length=>"))
bred = int(input("enter breadth=>"))
b=rectangle(leng,bred)
b.Area()
c=square(leng,bred)
c.Area()




