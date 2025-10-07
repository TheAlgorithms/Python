n=5
for i in range(1,n):
    for j in range(n):
        if j==1:
            print(" "*(n-i)+"*")
        else:
            print(" "*(n-i)+"*"+" "*(2*i-3)+"*")
for i in range(1,n+1):
    if i==1:
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")