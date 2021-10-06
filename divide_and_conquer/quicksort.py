def index(a,l,h):
    pivot=a[h]
    i=l
    for j in range(i,h+1):
        if a[j]<pivot:
            a[j],a[i]=a[i],a[j]
            i+=1

    a[i],a[h]=a[h],a[i]
    return i
def quicksort(a,l,h):
    if(l<=h):
        i=index(a,l,h)
        quicksort(a,l,i-1)
        quicksort(a,i+1,h)
        
n=int(input("Enter the number of elements: "))
a=[]
print("Enter the elements of the array one by one: ")
for i in range(n):
    b=int(input())
    a.append(b)
quicksort(a,0,n-1)
print(a)
