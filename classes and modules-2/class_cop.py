class cop:
    def __init__(self,na,ag,wr,exp,des):
        self.na=na
        self.ag=ag
        self.wr=wr
        self.exp=exp
        self.des=des

    def disp(self):
        print("Person Name=%s"%self.na)
        print("Age=%d"%self.ag)
        print("Work=%s"%self.wr)
        print("Experience=%d"%self.exp)
        print("Designation=%s"%self.des)

    def update(self):
        self.na = input("Enter your name:-")
        self.ag = int(input("Enter your Age:-"))
        self.wr = input("Enter your work:-")
        self.exp = int(input("Enter your Experience:-"))
        self.des = input("Enter your Designation:-")

class mission(cop):
    def add_mission(self,mis):
        self.mis=mis
        print("mission=%s"%self.mis)


a = input("Enter your name:-")
b = int(input("Enter your Age:-"))
c = input("Enter your work:-")
d = int(input("Enter your Experience:-"))
e = input("Enter your Designation:-")

b=mission(a,b,c,d,e)
b.disp()
n=input("Enter your mission:-")
b.add_mission(n)
m=int(input("if you want to change information,Enter the key Zero"))
if(m==0):
    b.update()
    b.disp()
else :
    b.disp()