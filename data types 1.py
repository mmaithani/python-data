#Q.1- Create a list with user defined inputs. 
#Ans:-
# n=[0,0,0,0]
# n[0]=int(input("Enter the element of 1st position="))
# n[1]=int(input("Enter the element of 2st position="))
# n[2]=int(input("Enter the element of 3st position="))
# n[3]=int(input("Enter the element of 4st position="))
# print(n)

#Q.2- Add the following list to above created list:
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
#Ans:-
#l1=["google","apple","facebook","microsoft","tesla"]
#print(n.extend (l1))
#print(n)

#Q.3- Count the number of time an object occurs in a list. 
#Ans-
#l1=[1,2,1,2]
#print(l1.count(1))

#Q.4- create a list with numbers and sort it in ascending order.
#Ans-
#l1=[6,5,3,8,7] 
#l1.sort()
#print(l1)

#Q.5- Given are two one-dimensional arrays A and B 
#which are sorted in ascending order. Write a program
#to merge them into a single sorted array C that
#contains every item from arrays A and B, in ascending 
#order. [List] 
#Ans:-
#l1=[4,3,2,1]
#l2=[8,7,6,5]
#l1.sort()
#l2.sort()
#l3=[]
#print(l3.extend(l1),l3.extend(l2))
#print(l3)

#Q.6-Implement a stack and queue using lists.
#Ans- Stack
# l1=[]
# l1.append(10)
# l1.append(20)
# l1.append(30)
# l1.append(40)
# print(l1)
# l1.pop()
# print(l1)
# l1.pop()
# print(l1)
# l1.pop()
# print(l1) 
# l1.pop()
# print(l1)
# l=[]
# l.append(40)
# l.append(30)
# l.append(20)
# l.append(10)
# print(l)
# print(l.reverse())
#Queue
# l.pop()
# print(l)
# l.pop()
# print(l)
# l.pop()
#print(l) 
#l.pop()
#print(l)

#OPTIONAL QUESTION

#Q.1- Count even and odd numbers in that list.
#Ans-
e=0
o=0
l1=[1,2,3,4,5,6,7]
for n in l1:
	if n%2==0:
		e=e+1
	else:
		o=o+1
print(e)
print(o)
	
		
