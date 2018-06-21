#delete dublictae from list
# def listt(l):
# 	final=[]
# 	for a in l:
# 		if a not in final:
# 			final.append(a)
			
# 	return final
# s=input()
# numbers=list(map(int,s.split()))
# listt([s])

#li=[]
# for i  in range(0,10):
# 	print("c")
# 	a=(input("print any number"))
li=[]
t=()
num=(input("enter the values saparated with comma"))								
print(num)
li=num.split(',')
t=tuple(li)															#convert list in tuple and store in tuple t
print(t)