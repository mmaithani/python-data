# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")
if choice=='1' or choice=='2' or choice=='3' or choice=='4':
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	if choice == '1':
		print(num1,"+",num2,"=", add(num1,num2))
	elif choice == '2':
   		print(num1,"-",num2,"=", subtract(num1,num2))
	elif choice == '3':
   		print(num1,"*",num2,"=", multiply(num1,num2))

	elif choice == '4':
   		print(num1,"/",num2,"=", divide(num1,num2))
else:
	print ("*****>your keyboard need to replace, \n******>beacause you never do choosing mistake.\n \3 TRY AGAIN \3")