def is_palindrome(s: str) -> bool:
    """
    Determine if the string s is a palindrome.

    >>> is_palindrome("A man, A plan, A canal -- Panama!")
    True
    >>> is_palindrome("Hello")
    False
    >>> is_palindrome("Able was I ere I saw Elba")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("Mr. Owl ate my metal worm?")
    True
    """
    # Since punctuation, capitalization, and spaces are often ignored while checking
    # palindromes, we first remove them from our string.
    s = "".join(character for character in s.lower() if character.isalnum())
    return s == s[::-1]


if __name__ == "__main__":
    s = input("Please enter a string to see if it is a palindrome: ")
    if is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")
