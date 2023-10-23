"""
Given an array of integers and an integer k, find the kth largest element in the array

https://stackoverflow.com/questions/251781
"""

def partition(elements: list[int],low: int,high: int) -> int:
    """
    Partitions list based on the pivot element.

    This function rearranges the elements in the input list 'arr' such that
    all elements greater than or equal to the chosen pivot are on the right side
    of the pivot, and all elements smaller than the pivot are on the left side.

    Args:
        arr: The list to be partitioned
        low: The lower index of the list
        high: The higher index of the list
    Returns:
        int: The index of pivot element after partitioning

        Examples:
        >>> partition([3,1,4,5,9,2,6,5,3,5],0,9)
        4
        >>> partition([7,1,4,5,9,2,6,5,8],0,8)
        1
        >>> partition(['apple', 'cherry', 'date','banana'], 0, 3)
        2
        >>> partition([3.1, 1.2, 5.6, 4.7], 0, 3)
        1
    """
    pivot=elements[high]
    i=low-1
    for j in range(low,high):
        if elements[j]>= pivot:
            i+=1
            elements[i], elements[j]=elements[j],elements[i]
    elements[i+1],elements[high]=elements[high],elements[i+1]
    return i+1
def kth_largest_element(elements: list[int], k: int) -> int:
    """
    Finds the kth largest element in a list.

    Args:
        nums : The list of numbers.
        k : The position of the desired kth largest element.

    Returns:
        int: The kth largest element.

    Examples:
        >>> kth_largest_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3)
        5
        >>> kth_largest_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 2.5)
        -1
        >>> kth_largest_element([2, 5, 6, 1, 9, 3, 8, 4, 7, 3, 5], 1)
        9
        >>> kth_largest_element([2, 5, 6, 1, 9, 3, 8, 4, 7, 3, 5], -2)
        -1
        >>> kth_largest_element([9, 1, 3, 6, 7, 9, 8, 4, 2, 4, 9], 11)
        1
        >>> kth_largest_element([1, 2, 4, 3, 5, 9, 7, 6, 5, 9, 3], 0)
        -1
        >>> kth_largest_element(['apple', 'cherry', 'date','banana'], 2)
        'cherry'
        >>> kth_largest_element([3.1, 1.2, 5.6, 4.7,7.9,5,0], 2)
        5.6
        >>> kth_largest_element([3.1, 1.2, 5.6, 4.7,7.9,5,0], 1.5)
        -1
    """
    if not 1 <= k <= len(elements):
        return -1
    low,high=0,len(elements)-1
    while low<=high:
        if low>len(elements)-1 or high<0:
            return -1
        pivot_index=partition(elements,low,high)
        if pivot_index==k-1:
            return elements[pivot_index]
        elif pivot_index>k-1:
            high=pivot_index-1
        else:
            low=pivot_index+1
    return -1
if __name__=="__main__":
    import doctest
    doctest.testmod()