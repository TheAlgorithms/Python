from collections import Counter
from typing import Any


def mode(input_list: list) -> list[Any]:  # Defining function "mode."
    """This function returns the mode(Mode as in the measures of
    central tendency) of the input data.
    The input list may contain any Datastructure or any Datatype.
    >>> input_list = [2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2]
    >>> mode(input_list)
    [2]
    >>> input_list = [3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 2, 2, 2]
    >>> mode(input_list)
    [2]
    >>> input_list = [3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 4, 4, 2, 2, 4, 2]
    >>> mode(input_list)
    [2, 4]
    >>> input_list = ["x", "y", "y", "z"]
    >>> mode(input_list)
    ['y']
    >>> input_list = ["x", "x" , "y", "y", "z"]
    >>> mode(input_list)
    ['x', 'y']
    """
    counts: list[int] = list((Counter(input_list)).values())
    return list({val for val in input_list if input_list.count(val) == max(counts)}).sort()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
