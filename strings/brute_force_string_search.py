# based in algorithm "Brute-Force Algorithm" for string manipulation
# of the book "Algorithms in C" by Robert Sedgewick

"""Brute force algorithm to search a substring pattern in a string."""
def brute_force_string_search(string: str, substring: str) -> int:
    """Return the match start if the pattern is reached or the size
    of string if not match substring.

    >>> brute_force_string_search("abcdef", "de")
    3
    >>> brute_force_string_search("home sweet home", "home")
    0
    >>> brute_force_string_search("monkey", "le")
    6
    """

    m: int = len(string)
    n: int = len(substring)

    for i in range(len(string)):
        for j in range(len(substring)):
            if j < m or i < n:
                # the for loop iterate while the pointer 'j' is smaller than the length of 'string'
                # or pointer 'i' is smaller than the length of 'substring'
                while string[i] != substring[j]:
                    # the loop while iterate while the 'substring' matches with the 'string' substring
                    i -= j-1
                    j = 0
                    if i == m: break

                if j == m:
                    # if the end of pattern is reached returns the match starting
                    return i-m
                else:
                    # if the end of the text is reached before the end of the pattern is ever reached
                    # returns the value
                    return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
