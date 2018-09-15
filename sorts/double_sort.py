print ("enter the list to be sorted")
a = [int(x) for x in input().split()]
n=len(a)
for i in range(0,int(((n-1)/2)+1)):
    for j in range(0,n-1):
        if a[j+1]<a[j]:
            temp=a[j+1]
            a[j+1]=a[j]
            a[j]=temp
        if (a[n-1-j]<a[n-2-j]):
            temp=a[n-1-j]
            a[n-1-j]=a[n-2-j]
            a[n-2-j]=temp
print ("the sorted list is")
print (a)