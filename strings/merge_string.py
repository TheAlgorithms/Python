# Foundational implementation from merge sort
# https://en.wikipedia.org/wiki/Merge_sort
"""
Python implementation of how to merge two string
For doctests run following command:
python -m doctest -v merge_string.py
or
python3 -m doctest -v merge_string.py

For manual testing run:
python merge_string.py
"""


class StringBuilder(object):
    def __init__(self, val: str) -> None:
        self.store = [val]

    def __iadd__(self, value):
        """appends a character to the sequence"""
        self.store.append(value)
        return self

    def __str__(self) -> str:
        """string representation from the built sequence"""
        return "".join(self.store)


def merge_string(str_1: str, str_2: str) -> str:
    """Merges two string into one
    :param str_1 : first input string
    :param str_2 : second input string
    Examples:
    >>> merge_string("abc","def")
    'adbecf'
    >>> merge_string("mnin","aso")
    'mansion'
    """
    if len(str_1) < 0 and len(str_2) < 0:
        return ""
    if len(str_1) < 0 and len(str_2):
        return str_2
    if len(str_2) < 0 and len(str_1):
        return str_1

    ret = StringBuilder("")
    i, j = 0, 0
    while i < len(str_1) and j < len(str_2):
        if i > j:
            ret += str_2[j]
            j += 1
            continue
        ret += str_1[i]
        i += 1
    while i < len(str_1):
        ret += str_1[i]
        i += 1

    while j < len(str_2):
        ret += str_2[j]
        j += 1

    return str(ret)


if __name__ == "__main__":
    print(merge_string("abc", "def"))
    print(merge_string("ae", "f"))
    print(merge_string("mnin", "aso"))
