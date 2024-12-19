def join(separator: str, separated: list[str]) -> str:
    """
    Custom implementation of the join() function.
    This function manually concatenates the strings in the list,
    using the provided separator, without relying on str.join().

    :param separator: The separator to place between strings.
    :param separated: A list of strings to join.

    :return: A single string with elements joined by the separator.

    :raises Exception: If any element in the list is not a string.

    Examples:
    >>> join("", ["a", "b", "c", "d"])
    'abcd'
    >>> join("#", ["a", "b", "c", "d"])
    'a#b#c#d'
    >>> join("#", "a")  # Single string instead of list
    Traceback (most recent call last):
        ...
    Exception: join() accepts only strings
    >>> join(" ", ["You", "are", "amazing!"])
    'You are amazing!'
    >>> join("#", ["a", "b", "c", 1])
    Traceback (most recent call last):
        ...
    Exception: join() accepts only strings
    >>> join("-", ["apple", "banana", "cherry"])
    'apple-banana-cherry'
    >>> join(",", ["", "", ""])
    ',,'
    """
    result = ""
    for i, word_or_phrase in enumerate(separated):
        # Check if the element is a string
        if not isinstance(word_or_phrase, str):
            raise Exception("join() accepts only strings")

        # Add the current word or phrase to the result
        result += word_or_phrase
        # Add the separator if it's not the last element
        if i < len(separated) - 1:
            result += separator

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()
