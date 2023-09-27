"""
This is pure Python implementation of comb sort algorithm.
Comb sort is a relatively simple sorting algorithm originally designed by Wlodzimierz
Dobosiewicz in 1980.  It was rediscovered by Stephen Lacey and Richard Box in 1991.
Comb sort improves on bubble sort algorithm.
In bubble sort, distance (or gap) between two compared elements is always one.
Comb sort improvement is that gap can be much more than 1, in order to prevent slowing
down by small values
at the end of a list.

More info on: https://en.wikipedia.org/wiki/Comb_sort

For doctests run following command:
python -m doctest -v comb_sort.py
or
python3 -m doctest -v comb_sort.py

For manual testing run:
python comb_sort.py
"""


def comb_sort(data: list) -> list:
    """Pure implementation of comb sort algorithm in Python
    :param data: mutable collection with comparable items
    :return: the same collection in ascending order
    Examples:
    >>> comb_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> comb_sort([])
    []
    >>> comb_sort([99, 45, -7, 8, 2, 0, -15, 3])
    [-15, -7, 0, 2, 3, 8, 45, 99]
    """
    shrink_factor = 1.3
    gap = len(data)
    completed = False

    while not completed:
        # Update the gap value for a next comb
        gap = int(gap / shrink_factor)
        if gap <= 1:
            completed = True

        index = 0
        while index + gap < len(data):
            if data[index] > data[index + gap]:
                # Swap values
                data[index], data[index + gap] = data[index + gap], data[index]
                completed = False
            index += 1

    return data


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(comb_sort(unsorted))
