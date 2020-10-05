# This is a wonderful math problem . Link is https://codeforces.com/contest/1422/problem/C

MOD=10**9+7

digits=[int(x) for x in input()]
n=len(digits)


right=[0 for _ in range(n)]
r=0
mul=1
for i in range(n-1,-1,-1):
    r+=digits[i]*mul
    mul*=10
    mul%=MOD
    r%=MOD
    right[i]=r


left=[0 for _ in range(n)]
l=0
tot=0
for i in range(n):
    l*=10
    l+=digits[i]
    l%=MOD
    tot+=l
    tot%=MOD
    left[i]=tot

ans=0
for rr in range(1,n+1):
    leftIdx=rr-2#must have gap
    if leftIdx==-1 and rr==n: #len of input is 1
        break
    if leftIdx==-1:
        ans+=1*right[rr]
        ans%=MOD
    elif rr==n:
        nLeft=leftIdx+2
        ans+=left[leftIdx]
        ans%=MOD
    else:
        nLeft=leftIdx+2
        ans+=(left[leftIdx]%MOD)*pow(10,n-rr,MOD)+(nLeft*right[rr])%MOD
        ans%=MOD

#print(ans)
