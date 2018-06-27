# Q.1-  Write a Python program to read
      # last n lines of a file

f=open("abc.txt","r")
count=0
a=0
for line in f:
    count+=1

f.seek(0)
for line in f:
    a+=1
    if a>=count-5:
        print(line)
f.close()