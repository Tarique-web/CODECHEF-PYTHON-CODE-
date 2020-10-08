t=int(input())
while t!=0:
	n=int(input())
	a=[]
	while n!=0:
		a.append(n%2)
		n//=2
	b=len(a)
	s=""
	while b!=0:
		s+=str(a[b-1])
		b-=1
	print(s)
	t-=1