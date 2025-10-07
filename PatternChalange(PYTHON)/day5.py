n=5
t=0
for i in range(n*2):
    if i> n:
        t=2*n-i
    else:
        t=i
    for j in range(t):
        print("*",end=" ")
    print()