# 1. accepts the gender in terms of male or female from user. (if client enters wrong input instead of putting error it will display an appropriate msg)
#
# 2. Accept the name, and prints the name with salutation according to gender like sir for male and mam for female...
#
# 3. Ask the age and check the age criteria, if the age of man is greater than 20, it  will print you are  able  to enroll for python fundamental
# course otherwise it will display an msg that you are below age criteria you can't enroll the course..(program does not throw any kind of error here.)
#
# 4.if Age of women is greater than 19 she is available to enroll for core Java course.(same criteria error will not displayed)
#
# 5. If user enters wrong value like in case of input of name of he enters numeric value it will guide the user to enter alphabetic value.
#
# And in case of age of he enters alphabetical value it will only accepts integers and will guide the user to do so.
#
# Output will show looks like.... 👇🏻👇🏻👇🏻
#
# Condition required :- at any case all validations must be provided. Program will not throw any kind of error in any case...

print("hi ! i am your bot")
g=input('Enter your gender if male  press m/M and for female press f/F=>')
if g==m:
	name_m=input('Hi! Mr. whats your good  name=>')
    print("great ",name_m)
else:
    name_f=input("hello young lady can i get your name=>")
    print("ok ",name_f)


