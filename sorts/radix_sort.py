"""
This is a pure Python implementation of the quick sort algorithm
For doctests run following command:
python -m doctest -v radix_sort.py
or
python3 -m doctest -v radix_sort.py
For manual testing run:
python radix_sort.py
"""
from __future__ import annotations


def radix_with_bucket_sort(list_of_ints: list[int]) -> list[int]:
    """
    Examples:
    >>> radix_with_bucket_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> radix_with_bucket_sort(list(range(15))) == sorted(range(15))
    True
    >>> radix_with_bucket_sort(list(range(14,-1,-1))) == sorted(range(14,-1,-1))
    True
    >>> radix_with_bucket_sort([1,100,10,1000]) == sorted([1,100,10,1000])
    True
    """
    RADIX = 10
    placement = 1
    max_digit = max(list_of_ints)
    while placement <= max_digit:
        # declare and initialize empty buckets
        buckets: list[list] = [list() for _ in range(RADIX)]
        # split list_of_ints between the buckets
        for i in list_of_ints:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        # put each buckets' contents into list_of_ints
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                list_of_ints[a] = i
                a += 1
        # move to next
        placement *= RADIX
    return list_of_ints

def radix_with_counting_sort(list_of_ints: list[int]) -> List[int]:
    """
    This is much more standard inmplementation
    of radix sort compared to radix sort with buckets
    Examples:
    Examples:
    >>> radix_with_counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> radix_with_counting_sort(list(range(15))) == sorted(range(15))
    True
    >>> radix_with_counting_sort(list(range(14,-1,-1))) == sorted(range(14,-1,-1))
    True
    >>> radix_with_counting_sort([1,100,10,1000]) == sorted([1,100,10,1000])
    True
    """
    RADIX = 10
    placement = 1
    max_digit = max(list_of_ints)
    while placement <= max_digit:
        # declare list of counters
        counters: list[list] = [0] * (RADIX) # We need only 10 counters, for each digit from 0 - 9
        for element in list_of_ints:
            index = int((element / placement) % RADIX)
            counters[index] += 1 # We increes number of ocurances for particular digit

        # This is the hack!
        # Each counter has to be equal to it's value 
        # plus the sum of all values before him 
        # e.g. after initial count we have [0, 2, 4, 5, 1, 1, 0, 1, 2, 9]
        # we need to convert it to [0, 2, 6, 11, 12, 13, 13, 14, 16, 25]
        for index in range(1, RADIX):
            counters[index] += counters[index - 1]
        
        # Now each value in counter points to index + 1 in new, sorted, list
        # So we sort it, but the trick is to do it in reverse order
        new_list = [0] * (len(list_of_ints))
        for element_index in range(len(list_of_ints) - 1, -1, -1):
            index = int((list_of_ints[element_index] / placement) % RADIX)
            new_list_index = counters[index] - 1
            new_list[new_list_index] = list_of_ints[element_index]
            counters[index] -= 1
        
        list_of_ints = new_list
        del new_list
        placement *= RADIX
    return list_of_ints

if __name__ == "__main__":
    import doctest

    doctest.testmod()
