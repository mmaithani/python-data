object oriented programming(assignment)

1.requirement gathering
2. requirement analysis
3.Designing

for example : we can take blueprint of house as a class.
             and house made by that blueprint(class) is object,although all the houses(object) are same
             and the person who come to house for living is function of object
             if houses are not made still the blueprint is valid for further use
             so class remain individually
oop feature
 class
 object
 inheritance
 abstraction
 encapsulation
 polymorphism

which do not use thhese type of feature is call object based programming
......................................................................................................................



 ques.1: Create a Circle Class and Initialize it with Radius.

Ans.1
another method
 class Circle:
    def m(self,r):
        self.t=r
    def area(self):
        print(3.14*self.t*self.t)
x=int(input("enter radius of circle"))
a=Circle()
a.m(x)
a.area()

class circle:
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
            areaa = 3.14 * radius * radius
            print("Area of circle=>",areaa)
    def getcircum(self):
        print("Area of circumference=>",2*3.14*radius)

radius=int(input("enter radius for finding area and circumference=>"))
a=circle(radius)
a.getarea()
a.getcircum()

ques.2: Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def showname(self):
        print("your name is=>",self.name)
    def showroll(self):
        print("roll number=>",self.roll)
namee=(input("Enter your name=>"))
rolll=int(input("enter roll number too=>"))

a=Student(namee,rolll)
a.showname()
a.showroll()

Q.3- Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature:
    def __init__(self,cel,far):
        self.cel=cel
        self.far=far

    def convertfahr(self):
         print("temperature celcius to fahrenheit=>",self.cel*9/5+32)
    def convertcel(self):
        print("fahrenheit to celsius=>",self.far-32.5/9)
cell=int(input("enter temperature in celcius=>"))
farr=int(input("enter temperature in fahrenheit=>"))

a=Temperature(cell,farr)
a.convertfahr()
a.convertcel()

Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
Make methods to
1. Display-Display the details.
2. Update- Update the movie details.

class Moviedetails:
    def __init__(self, movie, artist, releaseyear, rating):

        self.movie = movie
        self.artist = artist
        self.releaseyear = releaseyear
        self.rating = rating

    def moviename(self):
        print("\n\n","Movie name is =>", name)

    def artistname(self):
        print("artist name is=>", artist)

    def release(self):
        print("year of release is=>", release)

    def ratingg(self):
        print("your rating for movie is =>", rating)

    def update(self, movie, artist, releaseyear, rating):

        self.movie = movie
        self.artist = artist
        self.releaseyear = releaseyear
        self.rating = rating

name=input("enter movie name=>")
artist=input("enter artist name=>")
release=input("enter year of release  of movie=>")
rating=(input("enter rating between 1 to 5"))

a=Moviedetails(name,artist,release,rating)
a.moviename()
a.artistname()
a.release()
a.ratingg()


name=input("enter movie name=>")
artist=input("enter artist name=>")
release=input("enter year of release  of movie=>")
rating=(input("enter rating between 1 to 5"))

a.update(name,artist,release,rating)
a.moviename()
a.artistname()
a.release()
a.ratingg()

#Q.5- Create a class Expenditure and initialize it with
expenditure,savings.Make the following methods.
1. Display expenditure and savings
2. Calculate total salary
3. Display salary
#Ans-
class expen:
    def __init__(self,exp,sav):
        self.expe=exp
        self.sa=sav

    def disp(self):
        print("Expenditure=%d"%self.expe)
        print("savings=%d"%self.sa)

    def  cal(self):
        self.sa=self.expe+self.sa

    def dips(self):
        print("Total salary:-%d"%self.sa)

e=int(input("Eneter the value of Expenditure:-"))
s=int(input("Eneter the value of Savings    :-"))
s=expen(e,s)
s.disp()
s.cal()
s.dips()


