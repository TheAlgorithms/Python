"""Gnome Sort Algorithm."""

from __future__ import print_function


def gnome_sort(unsorted):
    """Pure implementation of the gnome sort algorithm in Python."""
    if len(unsorted) <= 1:
        return unsorted

    i = 1

    while i < len(unsorted):
        if unsorted[i - 1] <= unsorted[i]:
            i += 1
        else:
            unsorted[i - 1], unsorted[i] = unsorted[i], unsorted[i - 1]
            i -= 1
            if (i == 0):
                i = 1


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    gnome_sort(unsorted)
    print(unsorted)
