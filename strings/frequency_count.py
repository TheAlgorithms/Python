def freq_chars(test_str):
    """
    This function iterates over characters of a string and keeps a counter and appends into a
    dictionary such that we get count of each charecter, So called frequecy of each element.
    >>> freq_chars('pythonpy')
    "Count of all characters in the test string is :{'p': 2, 'y': 2, 't': 1, 'h': 1, 'o': 1, 'n': 1}"
    >>> freq_chars('name')
    "Count of all characters in the test string is :{'n': 1, 'a': 1, 'm': 1, 'e': 1}"
    >>> freq_chars('gitHub')
    "Count of all characters in the test string is :{'g': 1, 'i': 1, 't': 1, 'H': 1, 'u': 1, 'b': 1}"
    """
    total_freq = {}
    for i in test_str:
        if i in total_freq:
            total_freq[i] += 1
        else:
            total_freq[i] = 1
    return "Count of all characters in the test string is :" + str(total_freq)


if __name__ == "__main__":

    from doctest import testmod

    testmod()
