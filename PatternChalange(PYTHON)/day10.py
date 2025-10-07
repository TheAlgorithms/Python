n=5
a=n
for i in range(1,n*2-2):
    if i==1 :
        print(" "*(n-i-1)+"*")
    elif i>n and i==n*2-3:
        print(" "*(i-(n-1))+"*")
    elif i>n-1:
        print(" "*(i-(n-1))+"*"+" "*(a-2)+"*")
        a-=2
    else:
        print(" "*(n-i-1)+"*"+" "*(2*i-3)+"*")