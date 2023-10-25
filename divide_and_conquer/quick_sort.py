"""
    Sorting Algorithm using Divide and Conquer method
    Quick_Sort
"""
def quicksort(arr, left, right):
    """
        Parameter: 
        arr: list
        left: start index for sorting
        right: end index for sorting
    """
    if(left<right):
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos-1)
        quicksort(arr, partition_pos+1, right)
        
def partition(arr, left, right):
    """
        Return a sorted index for pivot element
    """
    i = left
    j = right-1
    pivot = arr[right]
    while(i<j):
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
    if(arr[i] > pivot):
        arr[i], arr[right] = arr[right], arr[i]
    return i
