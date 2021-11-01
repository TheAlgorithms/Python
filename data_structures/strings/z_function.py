"""
https://cp-algorithms.com/string/z-function.html

Z-function or Z algorithm

Efficient algorithm for pattern occurrence in a string

Time Complexity: O(n) - where n is the length of the string

"""


def z_function(input_str: str) -> list:
    """
    For the given string this function computes value for each index,
    which represents the maximal length substring starting from the index
    and is the same as the prefix of the same size

    e.x.  for string 'abab' for second index value would be 2

    For the value of the first element the algorithm always returns 0

    >>> z_function("abracadabra")
    [0, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
    >>> z_function("aaaa")
    [0, 3, 2, 1]
    >>> z_function("zxxzxxz")
    [0, 0, 0, 4, 0, 0, 1]
    """
    z_result = [0] * len(input_str)

    # initialize interval's left pointer and right pointer
    left_pointer, right_pointer = 0, 0

    for i in range(1, len(input_str)):
        # case when current index is inside the interval
        if i <= right_pointer:
            min_edge = min(right_pointer - i + 1, z_result[i - left_pointer])
            z_result[i] = min_edge

        while go_next(i, z_result, input_str):
            z_result[i] += 1

        # if new index's result gives us more right interval,
        # we've to update left_pointer and right_pointer
        if i + z_result[i] - 1 > right_pointer:
            left_pointer, right_pointer = i, i + z_result[i] - 1

    return z_result


def go_next(i, z_result, s):
    """
    Check if we have to move forward to the next characters or not
    """
    return i + z_result[i] < len(s) and s[z_result[i]] == s[i + z_result[i]]


def find_pattern(pattern: str, input_str: str) -> int:
    """
    Example of using z-function for pattern occurrence
    Given function returns the number of times 'pattern'
    appears in 'input_str' as a substring

    >>> find_pattern("abr", "abracadabra")
    2
    >>> find_pattern("a", "aaaa")
    4
    >>> find_pattern("xz", "zxxzxxz")
    2
    """
    answer = 0
    # concatenate 'pattern' and 'input_str' and call z_function
    # with concatenated string
    z_result = z_function(pattern + input_str)

    for val in z_result:
        # if value is greater then length of the pattern string
        # that means this index is starting position of substring
        # which is equal to pattern string
        if val >= len(pattern):
            answer += 1

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
