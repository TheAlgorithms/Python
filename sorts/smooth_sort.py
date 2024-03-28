"""
This is a pure Python implementation of the smoothSort algorithm
Smooth Sort is an algorithm combine the concept of heap sort and the
concept of merge sort It was designed by Edsger W. Dijkstra
and later refined by Steven J. Ross.

More info on: https://en.wikipedia.org/wiki/Smoothsort

For doctests run following command:
python -m doctest -v smooth_sort.py
or
python3 -m doctest -v smooth_sort.py
For manual testing run:
python bogo_sort.py
"""


def smooth_sort(unsorted):
    """
    Pure implementation of the smooth sort algorithm using Leonardo numbers in Python
    :param unsorted: unordered mutable collection
    :return: the same collection ordered in ascending order

    Examples:
    >>> smooth_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> smooth_sort([])
    []

    >>> smooth_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def leonardo(leonardo_number):
        """
        leonardo number represent numbers in pattern where third number is the sum of
        2 preceding numbers plus 1 also leonardo number used in heap construction
        every number represent size of tree within the heap
        they are used in heapify using max heap approach which we will see later
        """
        if leonardo_number < 2:
            return 1
        return leonardo(leonardo_number - 1) + leonardo(leonardo_number - 2) + 1

    def heapify(start, end):
        i = start
        j = 0
        k = 0

        while k < end - start + 1:
            if k & 0xAAAAAAAA:
                j = j + i
                i = i >> 1
            else:
                i = i + j
                j = j >> 1

            k = k + 1

        while i > 0:
            j = j >> 1
            k = i + j
            while k < end:
                if unsorted[k] < unsorted[k - i]:
                    break
                unsorted[k], unsorted[k - i] = unsorted[k - i], unsorted[k]
                k = k + i

            i = j

    n = len(unsorted)
    if n <= 1:
        return unsorted

    p = n - 1
    q = p
    r = 0
    while p > 0:
        if (r & 0x03) == 0:
            heapify(r, q)

        if leonardo(r) == p:
            r = r + 1
        else:
            r = r - 1
            q = q - leonardo(r)
            heapify(r, q)
            q = r - 1
            r = r + 1

        unsorted[0], unsorted[p] = unsorted[p], unsorted[0]
        p = p - 1

    for i in range(n - 1):
        j = i + 1
        while j > 0 and unsorted[j] < unsorted[j - 1]:
            unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
            j = j - 1

    return unsorted


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    try:
        user_input = input(
            "Enter numbers separated by a comma (or press Enter to exit):\n"
        ).strip()
        if not user_input:
            print(smooth_sort([]))
        else:
            unsorted = [int(item) for item in user_input.split(",")]
            print(smooth_sort(unsorted))
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
