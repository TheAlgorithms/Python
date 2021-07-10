def islower(s: str) -> bool:
    """
    Determine whether the string is lower case or not
    :param s:
    :return: Boolean
    >>> islower("a man a plan a canal panama".replace(" ", ""))
    True
    >>> islower("Hello")
    False
    >>> islower("Able was I ere I saw Elba")
    False
    >>> islower("new")
    True
    >>> islower("TEST")
    False
    """
    # Since Punctuation, capitalization, and spaces are usually ignored while checking
    # lower case,  we first remove them from our string.
    s = "".join([character for character in s if character.isalnum()])
    return s == s.lower()


if __name__ == "__main__":
    s = input("Enter string to determine whether its lower case or not: ").strip()
    if islower(s):
        print("Given string in lower case")
    else:
        print("Given string is not in lower case")
