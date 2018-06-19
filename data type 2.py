#Q.1- Write a program to create a tuple with different
 #   data types and do the following operations.
#1. Find the length of tuples
#Ans-
#tuple= ('sahil','goyal')
#print(len(tuple))

#Q.2-Find largest and smallest elements of a tuples.
 #Ans:-
#tuple =(2,5,6,8,7,)
#print(tuple)
#print(max(tuple))
#print(min(tuple))

#Q.3- Write a program to find the product of all
#elements of a tuple.
#Ans:-
#tp=(2,3,5,8,9)
#prod=(2*3*5*8*9)
#print(prod)





                                # Sets
#Q.1- Create two set using user defined values.

#1. Calculate difference between two sets.
#2. Compare two sets.
#3. Print the result of intersection of two sets.
#Ans-
# Difference
#s1= set([1,2,3])
#s2= set([5,6.7])
#s3=  s1 - s2
#print(s3)

#compare
#s1=set([1,2])
#s2=set([1,2])
#print("compare of two sets:-")
#if(s1==s2):
 #   print("they are equal of set")
#else :
    #print("they are not equal")


#instersection
#s1=set([1,2])
#s2=set([1,2])
#print(s1&s2)


                        #DICTIONARIES

#Q.1- Create a dictionary to store name and marks of 10
#students by user input.
#Ans-
#di= {}
#i=0
#while i<10:
 #  na= input( "Enter your name:-")
  #  ma=int(input("Enter your marks:-"))
   # di[na]=ma
   # i=i+1
#print(di)

#Q.2-Sort the dictionary created in previous question
# according to marks.
#Ans
#di= {}
#i=0
#while i<5:
 #   na= input( "Enter your name:-")
  #  ma=int(input("Enter your marks:-"))
   # di[na]=ma
   # i=i+1
#print(di)

#v= list(di.v())
#print(v)
#v.sort()
#print(v)

#Q.3- Count the number of occurrence of each letter in
#  word "MISSISSIPPI". Store count of every letter with
# the letter in a dictionary.
#Ans:-
l= list("mississippi")
d={}
d['m']=l.count('m')
d['i']=l.count('i')
d['p']=l.count('p')
d['s']=l.count('s')