n=int(input("n="))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()