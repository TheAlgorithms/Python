#!python3
"""
The problem is to find a given string has unique characters.
>>> isUniqueSet("Brick")
True
>>> isUniqueHash("Brick")
True

"""


def isUniqueSet(s: str) -> str:
    """
    This function uses a set to determine the string contains unique characters
    s -> string
    return type -> bool
    >>> isUniqueSet("train")
    True
    >>> isUniqueSet("test")
    False
    """

    hashSet = set()
    for i in s:
        if i in hashSet:
            return False
        hashSet.add(i)
    return True


def isUniqueHash(s: str) -> str:
    """
    This function uses ascii values as index to determine
    the string contains unique characters
    s -> string
    return type -> bool
    >>> isUniqueHash("train")
    True
    >>> isUniqueHash("test")
    False
    """

    if len(s) > 256:
        return False
    hash = [False] * 256
    for i in s:
        index = ord(i)
        if hash[index]:
            return False
        hash[index] = True
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
