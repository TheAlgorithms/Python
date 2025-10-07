n=5
for i in range(1,n):
    print(" "*i,"* "*(n+1-i))
for i in range(1,n+1):
    print(" "*((n+1)-i),"* "*i)