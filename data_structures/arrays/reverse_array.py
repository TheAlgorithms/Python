"""
In-place array reversal.
This algorithm reverses the elements of a list without using extra space.
"""

from typing import Any


def reverse_array(arr: list[Any]) -> list[Any]:
    """
    Reverses a list in-place.

    This function takes a list and reverses its elements using a two-pointer
    approach. The left pointer starts at the beginning of the list, and the
    right pointer starts at the end. The elements at these two pointers are
    swapped, and the pointers move towards the center until they meet or cross.

    Args:
        arr: The list to be reversed.

    Returns:
        The same list, now reversed. This allows for method chaining.

    Doctests:
    >>> reverse_array([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> reverse_array(['a', 'b', 'c', 'd'])
    ['d', 'c', 'b', 'a']
    >>> reverse_array([10.5, 20.2, 30.8])
    [30.8, 20.2, 10.5]
    >>> reverse_array(["apple", "banana", "cherry"])
    ['cherry', 'banana', 'apple']
    >>> reverse_array([1])
    [1]
    >>> reverse_array([])
    []
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap the elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        # Move the pointers towards the center
        left += 1
        right -= 1
    return arr


if __name__ == "__main__":
    # The doctest module runs the tests embedded in the function's docstring.
    # To run the tests, execute this script from the command line:
    # python -m doctest -v reverse_array.py
    import doctest

    doctest.testmod()

    # Example usage:
    print("\n--- Example Usage ---")
    sample_array = [10, 20, 30, 40, 50, 60]
    print(f"Original array: {sample_array}")
    reverse_array(sample_array)
    print(f"Reversed array: {sample_array}")
