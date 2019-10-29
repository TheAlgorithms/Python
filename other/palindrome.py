# Algorithms to determine if a string is palindrome

test_data = {
    "MALAYALAM": True,
    "String": False,
    "rotor": True,
    "level": True,
    "A": True,
    "BB": True,
    "ABC": False,
    "amanaplanacanalpanama": True,  # "a man a plan a canal panama"
}
# Ensure our test data is valid
assert all((key == key[::-1]) is value for key, value in test_data.items())


def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome(key) is value for key, value in test_data.items())
    True
    """

    start_i = 0
    end_i = len(s) - 1
    while start_i < end_i:
        if s[start_i] == s[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True


def is_palindrome_recursive(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome_recursive(key) is value for key, value in test_data.items())
    True
    """
    if len(s) <= 1:
        return True
    if s[0] == s[len(s) - 1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False


def is_palindrome_slice(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome_slice(key) is value for key, value in test_data.items())
    True
    """
    return s == s[::-1]


if __name__ == "__main__":
    for key, value in test_data.items():
        assert is_palindrome(key) is is_palindrome_recursive(key)
        assert is_palindrome(key) is is_palindrome_slice(key)
        print(f"{key:21} {value}")
    print("a man a plan a canal panama")
