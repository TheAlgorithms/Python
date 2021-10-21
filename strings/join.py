"""
Program to join a list of strings with a given separator
"""


def join(separator: str, separated: list) -> str:
    """
    >>> join("", ["a", "b", "c", "d"])
    'abcd'
    >>> join("#", ["a", "b", "c", "d"])
    'a#b#c#d'
    >>> join("#", "a")
    'a'
    >>> join(" ", ["You", "are", "amazing!"])
    'You are amazing!'
    >>> join("#", ["a", "b", "c", 1])
    Traceback (most recent call last):
    ...
    Exception: join() accepts only strings to be joined
    """
    joined = ""
    for word_or_phrase in separated:
        if not isinstance(word_or_phrase, str):
            raise Exception("join() accepts only strings to be joined")
        joined += word_or_phrase + separator
    return joined.strip(separator)


if "__name__" == "__main__":
    from doctest import testmod

    testmod()
