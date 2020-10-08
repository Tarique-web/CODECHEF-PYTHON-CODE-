List1=[]
TestCase=int(input())
for n in range(TestCase):
    List1.append(int(input()))
    n=len(List1)
    for i in range(n-1):
    	for j in range(n-1-i):
    		if List1[j]>List1[j+1]:
    			List1[j],List1[j+1]=List1[j+1],List1[j]
for i in List1:
    print(i)