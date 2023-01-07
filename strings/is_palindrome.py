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
    # return s == s[::-1] the slicing method
    # uses extra spaces we can
    # better with iteration method.

    end = len(s) // 2
    n = len(s)

    # We need to traverse till half of the length of string
    # as we can get access of the i'th last element from
    # i'th index.
    # eg: [0,1,2,3,4,5] => 4th index can be accessed
    # with the help of 1st index (i==n-i-1)
    # where n is length of string

    for i in range(end):
        if s[i] != s[n - i - 1]:
            return False
    return True


if __name__ == "__main__":
    s = input("Please enter a string to see if it is a palindrome: ")
    if is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")
