n=int(input())
list1=list(map(int,input().split()))
even=0
odd=0
i=0
while i<n:
	if list1[i]%2==0:
		even+=1
	else:
		odd+=1
	i+=1
if even>odd:
	print("READY FOR BATTLE")
else:
	print("NOT READY")