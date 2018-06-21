#delete dublictae from list
def listt(l):
	final=[]
	for a in l:
		if a not in final:
			final.append(a)
			
	return final
s=input()
numbers=list(map(int,s.split()))
listt([s])