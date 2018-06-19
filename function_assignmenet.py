# # #Q.1- Create a function to calculate the area of a circle by taking radius from user.
# #
# #
# # r=int(input("enter radius of circle:-"))
# # def area():
# #     areaa=3.14*r*r
# #     print(areaa)
# #
# # area()
#
#
# # #Q.2- Write a function “perfect()” that determines if parameter number is a perfect number.
# # #  Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
# # #[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
# #  #sum to the number. E.g., 6 is a perfect number because 6=1+2+3]
# # def perfect():
# #  for n in range(6,1000):
# #   sum1 = 0
##  for i in range(1, n):
# #       if(n % i == 0):
# #           sum1 = sum1 + i
# #   if (sum1 == n):
# #       print(n)
# # perfect()
#
#
# #q.3- print multiplication table of 12 using recursion
#
# num=12
# for i in range(1,11):
#     print(num, '*' ,i, '=' , num*i)


#Q.4_ Write a function to calculate power of a number raised to other ( a^b ) using recursion.
# total=1
# num=int(input("enter the number"))
# power = int(input("enter the power of number"))
# if power > 1:
#     total = num ** num
#     power=power-1
# print(total)

#Q.5 write factorial of any number

# num=int(input("enter number"))
# fact=1
# if num<0:
#     print("its negative number")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#        fact=fact*i
#     print("factorial is=",fact)

