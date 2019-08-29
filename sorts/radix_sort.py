"""
This is a pure python implementation of the radix sort algorithm.

For doctests run following command:
python -m doctest -v radix_sort.py
or
python3 -m doctest -v radix_sort.py

For manual testing run:
python radix_sort.py
"""


def radix_sort(lst):
    """
    :param lst: some mutable ordered collection with heterogeneous
    comparable integer inside
    :return: None

    Examples:
    >>> lst = [55, 9, 3889, 0, 677]
    >>> radix_sort(lst)
    >>> print(lst)
    [0, 9, 55, 677, 3889]
    """
    RADIX = 10
    placement = 1

    # get the maximum number
    max_digit = max(lst)

    while placement < max_digit:
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split lst between lists
        for i in lst:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        # empty lists into lst array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            if len(buck) != 0:
                for i in buck:
                    lst[a] = i
                    a += 1

        # move to next
        placement *= RADIX


if __name__ == "__main__":
    lst = [55, 9, 3889, 0, 677]
    radix_sort(lst)
    print(lst)

