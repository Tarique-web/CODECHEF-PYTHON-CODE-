t=int(input())
while t!=0:
    A=(input()).split()
    B=int(A[1])
    A=int(A[0])
    result=A%B
    print(result)
    t-=1