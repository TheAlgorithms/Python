"""
Gnome Sort Algorithm (A.K.A. Stupid Sort)

This algorithm iterates over a list, comparing each element with the previous one.
If the order is not respected, it swaps the element backward until the order is correct.
Then it resumes the iteration from the element's new position.

For doctests, run:
    python3 -m doctest -v gnome_sort.py

For manual testing, run:
    python3 gnome_sort.py
"""

from typing import List, TypeVar

T = TypeVar("T")  # Generic type for sorting any comparable data type


def gnome_sort(lst: List[T], reverse: bool = False) -> List[T]:
    """
    Pure implementation of the gnome sort algorithm in Python.

    Args:
        lst: A list of comparable items to be sorted.
        reverse: If True, sorts in descending order. Defaults to False.

    Returns:
        A sorted list.

    Examples:
    >>> gnome_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> gnome_sort([], reverse=True)
    []

    >>> gnome_sort([-2, -5, -45])
    [-45, -5, -2]

    >>> "".join(gnome_sort(list(set("Gnomes are stupid!"))))
    ' !Gadeimnoprstu'
    """
    n = len(lst)
    if n <= 1:
        return lst

    i = 1
    while i < n:
        if (not reverse and lst[i - 1] <= lst[i]) or (reverse and lst[i - 1] >= lst[i]):
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i = max(1, i - 1)

    return lst


if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by commas:\n").strip()
        unsorted = [float(x) for x in user_input.split(",") if x.strip()]
        order = input("Sort in descending order? (y/n): ").strip().lower() == "y"

        print("\nSorted result:", gnome_sort(unsorted, reverse=order))
    except ValueError:
        print("❌ Invalid input! Please enter numeric values separated by commas.")
