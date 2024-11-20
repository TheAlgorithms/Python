from sys import maxsize


def array_equalization(vector: list[int], step_size: int) -> int:
    """
    This algorithm equalizes all elements of the input vector
    to a common value, by making the minimal number of
    "updates" under the constraint of a step size (step_size).

    >>> array_equalization([1, 1, 6, 2, 4, 6, 5, 1, 7, 2, 2, 1, 7, 2, 2], 4)
    4
    >>> array_equalization([22, 81, 88, 71, 22, 81, 632, 81, 81, 22, 92], 2)
    5
    >>> array_equalization([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 5)
    0
    >>> array_equalization([22, 22, 22, 33, 33, 33], 2)
    2
    >>> array_equalization([1, 2, 3], 0)
    Traceback (most recent call last):
    ValueError: Step size must be positive and non-zero.
    >>> array_equalization([1, 2, 3], -1)
    Traceback (most recent call last):
    ValueError: Step size must be positive and non-zero.
    >>> array_equalization([1, 2, 3], 0.5)
    Traceback (most recent call last):
    ValueError: Step size must be an integer.
    >>> array_equalization([1, 2, 3], maxsize)
    1
    """
    if step_size <= 0:
        raise ValueError("Step size must be positive and non-zero.")
    if not isinstance(step_size, int):
        raise ValueError("Step size must be an integer.")

    unique_elements = set(vector)
    min_updates = maxsize

    for element in unique_elements:
        elem_index = 0
        updates = 0
        while elem_index < len(vector):
            if vector[elem_index] != element:
                updates += 1
                elem_index += step_size
            else:
                elem_index += 1
        min_updates = min(min_updates, updates)

    return min_updates


if __name__ == "__main__":
    from doctest import testmod

    testmod()
