TestCase=int(input())
for i in range(TestCase):
    C,D,L=map(int,input().split())
    
    max_lag=(C+D)*4
    
    if C<=(D*2):
        min_lag=(4*D)

    else:
        min_lag=(C-D)*4
    if (L%4==0 and L>=min_lag and L<=max_lag):
        print("yes")
    else:
        print("no")