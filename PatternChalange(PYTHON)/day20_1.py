n=int(input("n="))
for i in range(n,-1,-1):
    for j in range(i,-1,-1):
        print(chr(j+65),end=" ")
    print()    