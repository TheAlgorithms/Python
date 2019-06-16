# https://projecteuler.net/problem=234
def fib(a, b, n):
    
    if n==1:
        return a
    elif n==2:
        return b
    elif n==3:
        return str(a)+str(b)
    
    temp = 0
    for x in range(2,n):
        c=str(a) + str(b)
        temp = b
        b = c
        a = temp
    return c


q=int(input())
for x in range(q):
    l=[i for i in input().split()]
    c1=0
    c2=1
    while(1):
        
        if len(fib(l[0],l[1],c2))<int(l[2]):
            c2+=1
        else:
            break
    print(fib(l[0],l[1],c2+1)[int(l[2])-1])
 
