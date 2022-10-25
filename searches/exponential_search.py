"""
This is pure Python implementation of exponential search algorithm
For doctests run following command:
python3 -m doctest -v linear_search.py
For manual testing run:
python3 linear_search.py
"""

# A recursive binary search function returns location  of search_element in given array if present, otherwise -1
def binary_search( array: list, left: int, right: int, search_element: int) -> int:
    """A pure Python implementation of binary search algorithm
    :param array: a collection with comparable items (items are sorted)
    :param left: leftmost boundary of the array
    :param right: rightmost boundary of the array
    :param search_element: the element we are looking for in the array
    :return: index of found item or -1 if item is not found
    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0, 4, 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 0, 4, 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 0, 4, 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 0, 4, 6)
    -1
    """
    if right >= left:
        middle = left + ( right-left ) // 2
          
        # If the element is present at the middle itself
        if array[middle] == search_element:
            return middle
          
        # If the element is smaller than mid, then it can only be present in the left subarray
        if array[middle] > search_element:
            return binary_search(array, left, 
                                middle - 1, search_element)
          
        # Else he element can only be present in the right
        return binary_search(array, middle + 1, right, search_element)
          
    # We reach here if the search_element is not present
    return -1
  
# Returns the position of first occurrence of search_element in array
def exponential_search(array: list, no_of_items: int, search_element: int) -> int:
    """A pure Python implementation of exponential search algorithm
    :param array: a collection with comparable items (items are sorted)
    :param no_of_items: number of items in the array
    :param search_element: the element we are looking for in the array
    :return: index of found item or -1 if item is not found
    Examples:
    >>> exponential_search([0, 5, 7, 10, 15], 5, 0)
    0
    >>> exponential_search([0, 5, 7, 10, 15], 5, 15)
    4
    >>> exponential_search([0, 5, 7, 10, 15], 5, 5)
    1
    >>> exponential_search([0, 5, 7, 10, 15], 5, 6)
    -1
    """
    
    # IF search_element is present at first location itself
    if array[0] == search_element:
        return 0

    index = 1
    while index < no_of_items and array[index] <= search_element:
        index = index * 2
      
    # Call binary search for searching the element in the found range
    return binary_search( array, index // 2, 
                         min(index, no_of_items-1), search_element)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
