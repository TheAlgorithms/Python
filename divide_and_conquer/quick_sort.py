def index(a: list,low: int,high: int) ->int:
    """
    fuction returns the index position of
    where the pivot belongs to
    """

    pivot=a[high]      #any element can be selected as the pivot.In this case the last element is selected.
    i=low
    for j in range(i,high+1):
        if a[j]<pivot:
            a[j],a[i]=a[i],a[j]   #whenever an element lower than the pivot,i th and j th position elements are swapped.
            i+=1        

    a[i],a[high]=a[high],a[i]   #all elements till index position i(including i) will contain elements lesser than the pivot. 
    return i                    
def quick_sort(a: list,low: int,high: int):
    
    """
    This function is recursively called for index positions
    low to i-1 and i+1 to high
    
    """
    if(low<=high):
        i=index(a,low,high)
        quick_sort(a,low,i-1)  #The functions are called for either sides of the returned index i of the array.
        quick_sort(a,i+1,high)
        
n=int(input("Enter the number of elements: ").strip())
a=[]
print("Enter the elements of the array one by one: ")
for i in range(n):
    b=int(input())
    a.append(b)
quick_sort(a,0,n-1)
print(a)
