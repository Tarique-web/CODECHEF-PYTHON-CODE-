'''
Here I am finding GCD and LCM from Math formula of GCD & LCM
How many times we want to take input that's why we take test_cases varale for input
'''
test_cases=int(input())
for i in range(test_cases):
    # till loop condition is true that time take input
    number=input().split()
    
    x=int(number[0])
    
    y=int(number[1])
    
    Find_lcm = x * y
    
    while x!=y:
        
        if x>y:
            
            x=x-y
            
        else:
            
            y=y-x
    GCD=x
    print(GCD,Find_lcm//GCD)  