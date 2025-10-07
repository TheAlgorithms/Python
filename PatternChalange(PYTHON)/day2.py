n=5
for i in range(1,n):
    for j in range(i):
        if j<i:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()