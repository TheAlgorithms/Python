#!python3
"""
The problem is to find a given string has unique characters.
>>> isUniqueSet("Brick")
True
>>> isUniqueHash("Brick")
True

"""


def isUniqueSet(string: str) -> bool:
    """
    This function uses a set to determine the string contains unique characters
    >>> isUniqueSet("train")
    True
    >>> isUniqueSet("test")
    False
    """

    hashSet = set()
    for i in string:
        if i in hashSet:
            return False
        hashSet.add(i)
    return True


def isUniqueHash(string: str) -> bool:
    """
    This function uses ascii values as index to determine
    the string contains unique characters
    >>> isUniqueHash("train")
    True
    >>> isUniqueHash("test")
    False
    """

    if len(string) > 256:
        return False
    hash = [False] * 256
    for i in string:
        index = ord(i)
        if hash[index]:
            return False
        hash[index] = True
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
