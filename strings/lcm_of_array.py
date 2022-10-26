def isprime(n):
    if n==1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
    return True
def gcd(a,b):
    if isprime(a) and isprime(b):
        return 1
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
n=int(input())
lst=list(map(int,input().split()))
lcm=lst[0]
for i in range(1,len(lst)):
    #print(i)
    lcm=((lst[i]*lcm)//(gcd(lst[i],lcm)))
    #print(gcd(lst[i],lcm))
print(lcm)
