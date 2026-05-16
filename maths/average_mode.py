from typing import Any


def mode(input_list: list) -> list[Any]:
    """This function returns the mode(Mode as in the measures of
    central tendency) of the input data.

    The input list may contain any Datastructure or any Datatype.

    >>> mode([2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2])
    [2]
    >>> mode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 2, 2, 2])
    [2]
    >>> mode([3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 4, 2, 2, 4, 2])
    [2, 4]
    >>> mode(["x", "y", "y", "z"])
    ['y']
    >>> mode(["x", "x" , "y", "y", "z"])
    ['x', 'y']
    """
    if not input_list:
        return []
    result = [input_list.count(value) for value in input_list]
    y = max(result)  # Gets the maximum count in the input list.
    # Gets values of modes
    return sorted({input_list[i] for i, value in enumerate(result) if value == y})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
