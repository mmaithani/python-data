               #ASSIGNMENT-6
                   #LOOPS
#Let’s iterate your minds with loops.

#Q.1- Take 10 integers from user and print it on screen.
#Ans-
#i=1
#while i<=10 :
 #   n=int(input("Enter the value ;-"))
  #  print(n)
   # i=i+1

#Q.2- Write an infinite loop.An infinite loop never ends.
      #         Condition is always true.
      #Ans-
#i=1
#while i==1:
    #print("hello world")

#Q.3- Create a list of integer elements by user input.
 #   Make a new list which will store square of elements of
  #previous list.
  #Ans:-
#x=int(input("Enter the value x :-"))
#y=int(input("Enter the value y :-"))
#z=int(input("Enter the value z :-"))
#l=[x,y,z]
#l2=[x**2,y**2,z**2]
#print(l2)

#Q.4- From a list containing ints, strings and floats,
               #  make three lists to store them separately

#Ans-
#l1=[1,2,3,'a','b','c',1.1,2.2,3.3]
#li = []
#ls = []
#lf = []

#print(isinstance(l1[0],int))

#for x in l1:
 #   if type(x) == int:
  #      li.append(x)
   # elif type(x) == str:
    #    ls.append(x)
    #elif type(x) == float:
     #   lf.append(x)
    #else:
     #   print("Value is not int,str or float")
#print(li,ls,lf,sep="\n")

#Q.5- Using range(1,101), make a list containing even
               # and odd numbers.
     #Ans-

#l1=[]
#l2=[]
#for n in range(1,101) :
 #  if n%2 ==0:
  #   l1.append(n)
  # else :
  #  l2.append(n)
#print ("even number :-",l1)
#print("odd number:-",l2)

#Q.6- Print the following patterns:
#*
#**
#***
#****
#Ans-
#for n in range(5):
 #   j=1
  #  while j<=n:
   #    print("*",end="")
    #   j=j+1
    #print()

#Q.7- Create a user defined dictionary and get keys
               #corresponding to the value using for loop.
 #Ans-
#x= int(input("Enter the key x:-"))
#y=int(input("Enetr the key y:-"))
#z= int(input("Enter the key z:-"))
#d = {x:'a',y:'b',z:'c'}

#for x in d:
 #   print(x)


#Q.8- Take inputs from user to make a list. Again take
 # one input from user and search it in the list and delete
               # that element, if found. Iterate over list using for loop.
               #Ans-

x= int(input("Enter the key x:-"))
y=int(input("Enetr the key y:-"))
z= int(input("Enter the key z:-"))
l=[x,y,z]
k= int(input("Enter the key of search :-"))
for n in range(3):
    if (l[n]==k):
        print("Value found",n)
        del l[n]
        break;
print(l)

