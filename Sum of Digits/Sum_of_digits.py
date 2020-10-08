n=int(input())
while n!=0:
	n1=int(input())
	s=0
	while n1!=0:
		r=(n1%10)
		s+=r
		n1//=10
	n-=1
	print(s)