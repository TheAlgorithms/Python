def index(arr: list,low: int,high: int) ->int:
    """
    fuction returns the index position of
    where the pivot belongs to
    """

    pivot=arr[high]      #any element can be selected as the pivot.In this case the last element is selected.
    i=low
    for j in range(i,high+1):
        if arr[j]<pivot:
            arr[j],arr[i]=arr[i],arr[j]   #whenever an element lower than the pivot,i th and j th position elements are swapped.
            i+=1        

    arr[i],arr[high]=arr[high],arr[i]   #all elements till index position i(including i) will contain elements lesser than the pivot. 
    return i                    
def quick_sort(arr: list,low: int,high: int) ->None:
    
    """
    This function is recursively called for index positions
    low to i-1 and i+1 to high
    
    """
    if(low<=high):
        i=index(arr,low,high)
        quick_sort(arr,low,i-1)  #The functions are called for either sides of the returned index i of the array.
        quick_sort(arr,i+1,high)
        
num=int(input("Enter the number of elements: ").strip())
arr=[]
print("Enter the elements of the array one by one: ")
for i in range(num):
    b=int(input())
    arr.append(b)
quick_sort(arr,0,num-1)
print(arr)
