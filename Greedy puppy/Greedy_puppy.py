TestCase=int(input())
for i in range(TestCase):
    N,K=map(int,input().split())
    tuzik=1
    for i in range(1,K+1):
    	rem=N%i
    	if rem>=tuzik:
    		 
    		if tuzik!=0:
    			tuzik=rem
    			
    		  	
    	
    print(tuzik)