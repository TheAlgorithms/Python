"""
Program to join a list of strings with a given separator
"""


def join(separator: str, separated: list[str]) -> str:
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
    try:
        return separator.join(separated)
    except TypeError:
        raise Exception("join() accepts only strings to be joined")

if __name__ == '__main__':
    from doctest import testmod
    testmod()
