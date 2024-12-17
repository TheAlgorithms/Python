"""
Program to join a list of strings with a separator
"""


def join(separator: str, separated: list[str]) -> str:
    """
    Joins a list of strings using a separator
    and returns the result.

    :param separator: Separator to be used
                for joining the strings.
    :param separated: List of strings to be joined.

    :return: Joined string with the specified separator.

    Examples:

    >>> join("", ["a", "b", "c", "d"])
    'abcd'
    >>> join("#", ["a", "b", "c", "d"])
    'a#b#c#d'
    >>> join("#", "a")
    'a'
    >>> join(" ", ["You", "are", "amazing!"])
    'You are amazing!'

    This example should raise an
    exception for non-string elements:
    >>> join("#", ["a", "b", "c", 1])
    Traceback (most recent call last):
        ...
    Exception: join() accepts only strings

    Additional test case with a different separator:
    >>> join("-", ["apple", "banana", "cherry"])
    'apple-banana-cherry'
    """

    joined: str = ""
    """
    The last element of the list is not followed by the separator.
    So, we need to iterate through the list and join each element
    with the separator except the last element.
    """
    last_index: int = len(separated) - 1
    """
    Iterate through the list and join each element with the separator.
    Except the last element, all other elements are followed by the separator.
    """
    for index in range(last_index):
        """
        If the element is not a string, raise an exception.
        """
        if not isinstance(separated[index], str):
            raise Exception("join() accepts only strings")
        """
        join the element with the separator.
        """
        joined += separated[index] + separator
    """
    If the list is not empty, join the last element.
    """
    if separated != []:
        """
        If the last element is not a string, raise an exception.
        """
        if not isinstance(separated[len(separated) - 1], str):
            raise Exception("join() accepts only strings")
        joined += separated[len(separated) - 1]
    """
    RETURN the joined string.
    """
    return joined


if __name__ == "__main__":
    from doctest import testmod

    testmod()
