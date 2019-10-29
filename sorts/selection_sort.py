"""
This is a pure python implementation of the selection sort algorithm

For doctests run following command:
python -m doctest -v selection_sort.py
or
python3 -m doctest -v selection_sort.py

For manual testing run:
python selection_sort.py
"""


def selection_sort(a):
    """Pure implementation of the selection sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending


    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> selection_sort([4,5,3,2,4,1])
    [1,2,3,4,4,5]
    """

    # Traverse through all array elements 
    for i in range(len(a)): 
  
        # Find the minimum element in remaining 
        # unsorted array 
        min_idx = i 
        for j in range(i + 1, n): 
            if a[min_idx] > a[j]: 
                min_idx = j 
  
        # Move minimum element at current i 
        key = a[min_idx] 
        while min_idx > i: 
            a[min_idx] = a[min_idx - 1] 
            min_idx -= 1
        a[i] = key 
    return a


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(selection_sort(unsorted))
