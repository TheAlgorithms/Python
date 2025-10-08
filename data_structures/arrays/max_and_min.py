"""
Find the maximum and minimum elements in a list.
Source: https://en.wikipedia.org/wiki/Maximum_and_minimum

>>> find_max_min([4, 2, 9, 1, 7])
(9, 1)
>>> find_max_min([-5, -10, 0, 5])
(5, -10)
>>> find_max_min([42])
(42, 42)
>>> find_max_min([])
"""


def find_max_min(arr: list[int]) -> tuple[int | None, int | None]:
    """
    Returns the maximum and minimum elements of a list.

    Parameters:
    arr (list[int]): The list of numbers.

    Returns:
    tuple[int | None, int | None]: (maximum, minimum), or (None, None) if the list is empty.
    """
    if not arr:
        raise ValueError("find_max_min() arg is an empty list")
    maximum = max(arr)
    minimum = min(arr)
    return maximum, minimum


if __name__ == "__main__":
    examples = [
        [4, 2, 9, 1, 7],
        [-5, -10, 0, 5],
        [42],
    ]

    for arr in examples:
        max_val, min_val = find_max_min(arr)
        print(f"For list {arr}, maximum: {max_val}, minimum: {min_val}")
