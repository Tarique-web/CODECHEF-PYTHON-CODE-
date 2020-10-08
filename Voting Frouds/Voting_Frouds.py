t=int(input())
while t!=0:
	n=int(input())
	list1=list(int(num) for num in input().split())[:n]

	b=[]
	c=0
	for i in list1:
		if i not in  b:
			b.append(i)					
		else:
			c+=1				
	t-=1
	print(c)