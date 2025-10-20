"""
A pure Python implementation of the quick sort algorithm with optimizations

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""

from __future__ import annotations

from random import randrange


def insertion_sort(collection: list, left: int, right: int) -> None:
    """Insertion sort for small arrays (optimization for quicksort).
    
    Args:
        collection: List to sort
        left: Starting index
        right: Ending index (inclusive)
    """
    for i in range(left + 1, right + 1):
        key = collection[i]
        j = i - 1
        while j >= left and collection[j] > key:
            collection[j + 1] = collection[j]
            j -= 1
        collection[j + 1] = key


def median_of_three(collection: list, left: int, mid: int, right: int) -> int:
    """Return the index of the median of three elements.
    
    Args:
        collection: List to find median in
        left: Left index
        mid: Middle index  
        right: Right index
        
    Returns:
        Index of the median element
    """
    a, b, c = collection[left], collection[mid], collection[right]
    if (a <= b <= c) or (c <= b <= a):
        return mid
    elif (b <= a <= c) or (c <= a <= b):
        return left
    else:
        return right


def partition_hoare(collection: list, left: int, right: int) -> int:
    """Hoare partition scheme for quicksort.
    
    Args:
        collection: List to partition
        left: Left boundary
        right: Right boundary
        
    Returns:
        Final position of pivot
    """
    # Use median of three for better pivot selection
    mid = left + (right - left) // 2
    pivot_idx = median_of_three(collection, left, mid, right)
    
    # Move pivot to the beginning
    collection[left], collection[pivot_idx] = collection[pivot_idx], collection[left]
    pivot = collection[left]
    
    i, j = left - 1, right + 1
    
    while True:
        i += 1
        while collection[i] < pivot:
            i += 1
            
        j -= 1
        while collection[j] > pivot:
            j -= 1
            
        if i >= j:
            return j
            
        collection[i], collection[j] = collection[j], collection[i]


def quick_sort_inplace(collection: list, left: int = 0, right: int = None) -> None:
    """Optimized in-place quicksort with multiple optimizations.
    
    Optimizations:
    - In-place partitioning (O(1) extra space vs O(n))
    - Median-of-three pivot selection
    - Hybrid with insertion sort for small arrays
    - Hoare partition scheme (better for duplicates)
    
    Args:
        collection: List to sort (modified in-place)
        left: Left boundary
        right: Right boundary
    """
    if right is None:
        right = len(collection) - 1
        
    if left < right:
        # Use insertion sort for small arrays (optimization)
        if right - left < 10:
            insertion_sort(collection, left, right)
            return
            
        # Partition and get pivot position
        pivot_pos = partition_hoare(collection, left, right)
        
        # Recursively sort left and right partitions
        quick_sort_inplace(collection, left, pivot_pos)
        quick_sort_inplace(collection, pivot_pos + 1, right)


def quick_sort(collection: list) -> list:
    """A pure Python implementation of quicksort algorithm.
    
    This is the original implementation kept for compatibility.
    For better performance, use quick_sort_optimized().

    :param collection: a mutable collection of comparable items
    :return: the same collection ordered in ascending order

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    # Base case: if the collection has 0 or 1 elements, it is already sorted
    if len(collection) < 2:
        return collection

    # Randomly select a pivot index and remove the pivot element from the collection
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    # Partition the remaining elements into two groups: lesser or equal, and greater
    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    # Recursively sort the lesser and greater groups, and combine with the pivot
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


def quick_sort_optimized(collection: list) -> list:
    """Optimized quicksort with in-place partitioning and multiple optimizations.
    
    Performance improvements:
    - O(1) extra space vs O(n) in original
    - Better pivot selection (median of three)
    - Hybrid with insertion sort for small arrays
    - More efficient partitioning
    
    Args:
        collection: List to sort
        
    Returns:
        Sorted list
        
    Examples:
    >>> quick_sort_optimized([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort_optimized([])
    []
    >>> quick_sort_optimized([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> quick_sort_optimized([3, 3, 3, 3, 3])
    [3, 3, 3, 3, 3]
    """
    if len(collection) < 2:
        return collection
        
    # Create a copy to avoid modifying the original
    result = collection.copy()
    quick_sort_inplace(result)
    return result


if __name__ == "__main__":
    # Get user input and convert it into a list of integers
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    # Print the result of sorting the user-provided list
    print(quick_sort(unsorted))
