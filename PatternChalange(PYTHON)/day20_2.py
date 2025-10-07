n=int(input("n="))
for i in range(n+1,-1,-1):
    for j in range(i,n+1):
        print(chr(65+j),end=" ")
    print()