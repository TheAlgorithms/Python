def partition(arr: list[float], left: int, right: int) -> int:
    """
        Picks a random (right most) element and sorts only the element.

            Parameters: 
                    arr (list[float]): List of numbers to be sorted.
                    left (int): starting index of list to be sorted.
                    right (int): ending index of list to be sorted.
                
            Returns:
                    index (int): Index of the sorted element. 

        >>> partition([23,12,55,20,32], 0, 4)
        3
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

def quicksort(arr: list[float], left: int, right: int) -> list[float]:
    """
        Sorts a list of numbers using divide and conquer.
        For more information, https://en.wikipedia.org/wiki/Quicksort.

        Parameter: 
                arr (list[float]): list
                left (int): start index for sorting
                right (int): end index for sorting

        Returns:
                list[float]: sorted list

        >>>quicksort([23,12,55,20,32], 0, 4)
        [12,20,23,32,55]
    """

    if(left<right):
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos-1)
        quicksort(arr, partition_pos+1, right)
        return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()