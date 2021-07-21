import re


def is_contains_number(string: str) -> bool:
    """
    Determine whether the string contains a number or not
    :param string:
    :return: Boolean
    >>> is_contains_number("A5B")
    True
    >>> is_contains_number("ABC")
    False
    >>> is_contains_number("AAA1")
    True
    >>> is_contains_number("aa5aabc")
    True
    >>> is_contains_number("aaabc*")
    False
    """
    pat = re.compile(r"(\d+)")
    match = re.search(pat, string)
    if match:
        return True
    return False


if __name__ == "__main__":
    print(is_contains_number("aaabc*"))
