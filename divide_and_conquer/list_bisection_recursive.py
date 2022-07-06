import typing
def bisection_recursive(element_to_find:typing.Any, list_to_search:list[typing.Any], index:int =0) -> int:
    """The bisection quickly finds the (index of) the desired element in a sorted list. The sorting itself is not relevant, it merely must lend itself to Python's "<" operator.
    It is extremely efficient. The following demonstrates: 
    
    >>> import numpy as np
    >>> L = np.arange(5e8).astype(np.int64)
    >>> %time bisection_recursive(3, L)
    1 ms
    
    Rules: 
        1. Look up the element in the middle of the list (call it list_middle).
        2. If this is the sought element, add middle to index and return the answer.
        3. If the element_to_find > list_middle, then the element to find must be in the right half of the list. Otherwise it is in the left part.
        4. Call the bisection function itself on the relevant half of list_to_search and increase the index by the number of elements we discarted **to the left** (only different from zero if the relevant half is the right half).
    
    Example A)
        bisection_recursive(5, [1, 2, 5, 6, 7, 8, 9], 0) gets called
        list_to_search[3] = 6 > 5 = element_to_find, so the algorithm continues with the left part of the list
        bisection_recursive(5, [1, 2, 5], 0) gets called
        2 < 5, so the algorithm continues with the right part of the list, setting index to 1
        bisection_recursive(5, [2, 5], 1) gets called
        bisection_recursive(5, [2, 5], 1) returns 2
    >>> 2
    Example B)
        bisection_recursive(5, [-2, -1, 0, 1, 1.5, 2, 5, 6, 7, 8, 9], 0) gets called
        2 < 5, so the algorithm continues with the right part of the list, setting index to 5
        bisection_recursive(5, [2, 5, 6, 7, 8, 9], 5) gets called
        list_to_search[3] = 7 > 5 = element_to_find, so the algorithm continues with the left part of the list
        bisection_recursive(5, [2, 5, 6], 5) gets called
        bisection_recursive(5, [2, 5, 6], 5) returns 6
    >>> 6
    """
    middle = len(list_to_search)//2
    # Recursion end: Once we divided the list up into single elements, we have conquered, as either the element we look at is the right one or our element is not in the list. Either way, we are done.
    if len(list_to_search)==1:
        if list_to_search[0] != element_to_find:
            # If nonexisting element is being searched, return index of closest element in an error to make it clear that the search was not successful: 
            raise ValueError(f"{element_to_find} is not in the list, would be between index {index+middle} and {index+middle+1}")
        return index
    # Recursion step:
    if element_to_find >=list_to_search[middle]:
        return bisection_recursive(element_to_find, list_to_search[middle:], index+middle)
    else:
        return bisection_recursive(element_to_find, list_to_search[:middle], index)
    
if __name__ == "__main__":
    import doctest

    doctest.testmod()
