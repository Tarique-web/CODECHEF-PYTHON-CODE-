test_cases=int(input())
for i in range(test_cases):

	N,K=map(int,input().split())
	n=list(map(int,input().split()))[:N]
	if K==1:
		max1=n[0]
		min1=n[0]
		sum1=0
		Average=len(n)-2
		for i in n:
			if i>=max1:
				max1=i
			else:
				if i<=min1:
					min1=i
			sum1+=i
				
		sum1-=min1+max1
		Average=sum1/Average
		print(Average)
	else:
		sum1=0
		Average=len(n)
		for i in n:
			sum1+=i
		Average=sum1/Average
		print(Average)
# ------------OR------------------
test_cases=int(input())
for i in range(test_cases):

	N,K=map(int,input().split())
	n=[int(x) for x in input().split()]
	n.sort()
	Average=len(n)
	max1=n[-1]
	min1=n[0]	
	sum1=0
	for i in n:
		sum1+=i
	sum1-=max1+min1
	if K>=1:
		print(sum1/(Average-2))

	else:	

		sum1+=max1+min1
		print(sum1/Average)