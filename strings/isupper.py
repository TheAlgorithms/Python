def isupper(s: str) -> bool:
    """
    Determine whether the string is upper case or not
    :param s:
    :return: Boolean
    >>> isupper("a man a plan a canal panama".replace(" ", ""))
    False
    >>> isupper("Hello")
    False
    >>> isupper("Able was I ere I saw Elba")
    False
    >>> isupper("racecar")
    False
    >>> isupper("HELLO")
    True
    """
    # Since Punctuation, capitalization, and spaces are usually ignored while checking
    # upper case,  we first remove them from our string.
    s = "".join([character for character in s if character.isalnum()])
    return s == s.upper()


if __name__ == "__main__":
    s = input("Enter string to determine whether its upper or not: ").strip()
    if isupper(s):
        print("Given string in upper case")
    else:
        print("Given string is not in upper case")
