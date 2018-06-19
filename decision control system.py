              #ASSIGNMENT-5
       #DECISION CONTROL SYSTEM
       #Let’s teach Python how to make decisions.
	   
  #Q.1- Take an input year from user and decide whether 
  #it is a leap year or not.
  #Ans-
#n=int(input("Enter the year:-"))
#if n%400==0:
     # print("%d is a leap year "%n)  
# else:
   # print("%d is not a leap year"%n) 


   #Q.2- Take length and breadth input from user and 
#check whether the dimensions are of square or
#rectangle.
#Ans:- 
# l=int(input("Enter the length:- "))
# b=int(input("Enter the breadth:-"))
# if l==b:
 # print("Then  it is square")
# else:
 # print("Then is Rectangle")

 
 #Q.3- Take the input age of 3 people and determine 
#oldest and youngest among them.
 #Ans:-
 
# a=int(input("Enter the age 1 person:-"))
# b=int(input("Enter the age 2 person:-"))
# c=int(input("Enter the age 3 person:-"))
# if a>b and a>c :
 # print("The biggest age is A")
# elif b>a and b>c:
 # print("The biggest age of B")
# else:
 # print("The biggest age of C ") 
 
 # Q.4- Write an if statement that lets a competitor know which of these prizes they 
 # won based on the number of points they scored, which is stored in the integer  
 # variable points(your input). points can only take on positive integer values up to
                     # 200. 
# If they've won a prize, the message should state "Congratulations! You won a
# [prize name]!" with the prize name. If there's no prize, the message should state
                   # "Sorry! No prize this time."

                            # Points	Prize
                            # 1-50	No Prize
                            # 51-150	Wooden Dog
                           # 151-180	Book
                           # 181-200	Chocolates
						   
 #Ans-
# n= int(input("Enter number of scored:- "))
# if n<=50:
 # print("No prize")
# elif n<=150:
 # print("Wooden prize")
# elif n<=180:
 # print("Book")
# else:
 # print("chocolates")
 
 
#**Q.5- A shop will give discount of 10% if the cost of
# purchased quantity is more than 1000.Ask user for 
#quantity Suppose, one unit will cost 100. Judge and 
#print total cost for user.  
 #Ans:-
qty=int(input("Enter Quantity:- "))

totalexp=qty*100
if totalexp>1000 :
  dis =totalexp*0.1
  totalexp=totalexp-dis
  print("Cost is %d"%totalexp)
else :
 print ("Total cost is %d "%totalexp)

