from typing import Any


def mode(input_list: list) -> list[Any]:  # Defining function "mode."
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
    result = list()  # Empty list to store the counts of elements in input_list
    for x in input_list:
        result.append(input_list.count(x))
    if not result:
        return []
    y = max(result)  # Gets the maximum value in the result list.
    # Gets values of modes
    result = list({input_list[i] for i, value in enumerate(result) if value == y})
    return sorted(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
