n=int(input("n="))
k=(2*n)-1
l=0
h=k-1
val=n
matrx=[[0 for i in range(k)] for j in range(k)]
for i in range(n):
    for j in range(l,h+1):
        matrx[l][j]=val
    for j in range(l+1,h+1):
        matrx[j][i]=val
    for j in range(l+1,h+1):
        matrx[h][j]=val
    for j in range(l+1,h):
        matrx[j][h]=val
    l+=1
    h-=1
    val-=1

for i in range(k):
    for j in range(k):
        print(matrx[i][j],end=" ")
    print()