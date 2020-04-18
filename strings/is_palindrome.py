def is_palindrome(s):
    """
    Determine whether the string is palindrome
    :param s:
    :return: Boolean
    >>> is_palindrome("a man a plan a canal panama".replace(" ", ""))
    True
    >>> is_palindrome("Hello")
    False
    """
    return s == s[::-1]


if __name__ == "__main__":
    s = input("Enter string to determine whether its palindrome or not: ").strip()
    if is_palindrome(s):
        print("Given string is palindrome")
    else:
        print("Given string is not palindrome")
