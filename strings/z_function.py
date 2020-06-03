"""
https://cp-algorithms.com/string/z-function.html#:~:text=The%20Z%2Dfunction%20for%20this,Note.

For given string this algorithm computes value for each index,
which represents the maximal length substring starting from the index
and is same as the prefix of the same size

e.x.  for string 'abab' for second index value would be 2

The main adventage of the algoirthm is that it's linear, using dynamic programming

Time Complexity: O(n)  - where n is the length of the string


For the value of the first element the algorithm always returns 0

"""


def z_function(input_str: str) -> list:
    """
    Will convert the entire string to uppercase letters

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

        # if new index's result gives us more right interval, we've to update left_pointer and right_pointer
        if i + z_result[i] - 1 > right_pointer:
            left_pointer, right_pointer = i, i + z_result[i] - 1

    return z_result


# helping function which checks if following elements are equal or not
def go_next(i, z_result, s):
    return i + z_result[i] < len(s) and s[z_result[i]] == s[i + z_result[i]]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
