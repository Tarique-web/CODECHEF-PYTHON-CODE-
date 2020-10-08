t=int(input())
while t!=0:
    list1=input().split()
    a=int(list1[0])
    b=int(list1[1])
    c=int(list1[2])
    if a>=b>=c:

    	print(b)
    else:
        if a>=c>=b:
    	    print(c)
        else:
            if b>=a>=c:
        	    print(a)
            else:
                if b>=c>=a:
                	print(c)
                else:
                    if c>=b>=a:
                	    print(b)
                    else:
                        if c>=a>=b:
                    	    print(a)
    t-=1