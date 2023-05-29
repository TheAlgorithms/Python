# Algorithms to determine if a string is palindrome

from timeit import timeit

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


def is_palindrome_traversal(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome_traversal(key) is value for key, value in test_data.items())
    True
    """
    end = len(s) // 2
    n = len(s)

    # We need to traverse till half of the length of string
    # as we can get access of the i'th last element from
    # i'th index.
    # eg: [0,1,2,3,4,5] => 4th index can be accessed
    # with the help of 1st index (i==n-i-1)
    # where n is length of string
    return all(s[i] == s[n - i - 1] for i in range(end))


def is_palindrome_recursive(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome_recursive(key) is value for key, value in test_data.items())
    True
    """
    if len(s) <= 2:
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


def benchmark_function(name: str) -> None:
    stmt = f"all({name}(key) is value for key, value in test_data.items())"
    setup = f"from __main__ import test_data, {name}"
    number = 500000
    result = timeit(stmt=stmt, setup=setup, number=number)
    print(f"{name:<35} finished {number:,} runs in {result:.5f} seconds")


if __name__ == "__main__":
    for key, value in test_data.items():
        assert is_palindrome(key) is is_palindrome_recursive(key)
        assert is_palindrome(key) is is_palindrome_slice(key)
        print(f"{key:21} {value}")
    print("a man a plan a canal panama")

    # finished 500,000 runs in 0.46793 seconds
    benchmark_function("is_palindrome_slice")
    # finished 500,000 runs in 0.85234 seconds
    benchmark_function("is_palindrome")
    # finished 500,000 runs in 1.32028 seconds
    benchmark_function("is_palindrome_recursive")
    # finished 500,000 runs in 2.08679 seconds
    benchmark_function("is_palindrome_traversal")
