#delete dublictae from list

def listt(l):
	final=[]
	for a in l:
		if a not in final:
			final.append(a)		
	return final
print(listt([1,2,2,2,4,4,5,5,6,8,9,3,2,5,4,4,4,5,5,5,9]))


