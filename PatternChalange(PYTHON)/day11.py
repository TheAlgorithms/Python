n=int(input("n="))
lst=[]
for i in range(n):
    temp_lst=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp_lst.append(1)
        else:
            temp_lst.append(lst[i-1][j-1] + lst[i-1][j])
    lst.append(temp_lst)
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print(lst[i][k],end=" ")
    print()