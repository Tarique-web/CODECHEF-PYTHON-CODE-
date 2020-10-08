n=int(input())
i=2
c=0
while True:
	for j in range(2,int(i**.5)+1):
		if i%j==0:
			break		
	else:
		print(i)
		c+=1
		if n==c:
			break
	i+=1