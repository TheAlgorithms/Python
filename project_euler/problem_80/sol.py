import math
import decimal
from math import floor

def solution():
    n=100
    p=100
    tot=0

    for i in range(1,n+1):
        sm=0
        decimal.getcontext().prec=p+10
        fv=decimal.Decimal(i).sqrt()
        if fv-floor(fv)==0:
            continue
        else:
            fv=str(fv).replace('.','')
            fv=fv[0:p]
            fv=int(fv)
            j=0
            while(fv!=0):
                sm=sm+(fv%10)
                fv=fv//10
            tot+=sm
    return tot

res=solution()
print(res)
