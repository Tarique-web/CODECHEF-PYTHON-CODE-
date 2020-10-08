t=int(input())
while t!=0:
    list1=input().split()
    a=int(list1[0])
    b=int(list1[1])
    c=int(list1[2])
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
    t-=1