test_cases=int(input())
for i in range(test_cases):
    sum_factor=1
    n=int(input())
    if n>1:
    	for j in range(2,int(n**.5)+1):
    		if n%j==0:
    			sum_factor+=j+n/j
    	if sum_factor==n:
    		print("YES")
    	else:
    		print("NO")

    else:
    	print("NO")