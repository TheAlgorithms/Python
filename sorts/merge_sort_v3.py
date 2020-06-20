"""
Program for implementation of MergeSort
MergeSort :
    merge sort is a Divide and Conquer algorithm.
    It divides input array in two halves,
    calls itself for the two halves and then merges the two sorted halves.
"""
from typing import List


def mergeSort(arr: List[int]):
    """
    This Function implements merge sort
    this function finds the mid of array,
    divides array into two parts,
    recursively and join them in sorted order

    variables:
        left_array
        right_array
        mid
        i,j,k (support variables)
    testing:
        ------------------------
    >>> arr = [3, 2, 1]
    >>> mergeSort(arr)
    >>> arr
    [1, 2, 3]
    >>> arr = [3, 2, 1, 0, 1, 2, 3, 5, 4]
    >>> mergeSort(arr)
    >>> arr
    [0, 1, 1, 2, 2, 3, 3, 4, 5]
    """
    if len(arr) > 1:
        # Finding the mid of the array
        mid: int = len(arr) // 2
        # Dividing the array elements
        left_array: List = arr[:mid]
        right_array: List = arr[mid:]

        # recursive calls
        mergeSort(left_array)  # Sorting the first half
        mergeSort(right_array)  # Sorting the second half

        i: int = 0
        j: int = 0
        k: int = 0

        # Copy data to temp arrays left_array[] and right_array[]
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


def main():
    """
    driver code for local testing of the above code
    """
    arr: List = [12, 11, 13, 5, 6, 7]
    print("Given array is: {}".format(arr))
    mergeSort(arr)
    print("Sorted array is: {}".format(arr))


if __name__ == "__main__":
    # main()
    import doctest

    doctest.testmod()


# This code is contributed by Mahesh
# improved by @itsvinayak
