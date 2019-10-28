# DarkCoder
def arith_sum(a,n,d):
    an=a+(n-1)*d
    if d==0:
        sum=n*a
    else:
        sum=(n/2)*(a+an)
    return sum
start=int(input("enter the starting no."))
no_of_terms=int(input("enter the no of terms"))
common_diff=int(input("enter the common diff"))
sum=arith_sum(start,no_of_terms,common_diff)
print("arithmetic sum=",sum)
