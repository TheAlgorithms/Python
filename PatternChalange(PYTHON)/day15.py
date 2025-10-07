n=5
for i in range(1,n):
    for j in range(i):
        print((i+j)%2,end=" ")
    print()