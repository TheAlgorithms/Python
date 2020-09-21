#!python3
"""
The problem is to find a given string has unique characters.
>>> is_unique_set("Brick")
True
>>> is_unique_hash("Brick")
True

"""


def is_unique_set(string: str) -> bool:
    """
    This function uses a set to determine the string contains unique characters
    >>> is_unique_set("train")
    True
    >>> is_unique_set("test")
    False
    """

    hash_set = set()
    for i in string:
        hash_set.add(i)
    return len(string)==len(hash_set)


def is_unique_hash(string: str) -> bool:
    """
    This function uses ascii values as index to determine
    the string contains unique characters
    >>> is_unique_hash("train")
    True
    >>> is_unique_hash("test")
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
