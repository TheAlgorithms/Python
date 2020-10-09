a1,b1 = list(map(int,input().split()))
a = max(a1,b1)
b = min(a1,b1)
while(b!=0):
    a,b = b,a%b
print(a)
