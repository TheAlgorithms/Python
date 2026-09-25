# Reference : https://www.geeksforgeeks.org/dsa/find-two-non-repeating-elements-in-an-array-of-repeating-elements
def find_two_unique_numbers(arr: list[int]) -> tuple[int, int]:
    """
    Given a list of integers where every element appears twice except for two numbers,
    find the two numbers that appear only once.

    this method returns the tuple of two numbers that appear only once using bitwise XOR
    and using the property of x & -x to isolate the rightmost bit
    (different bit between the two unique numbers).

    >>> find_two_unique_numbers([1,2,3,4,1,2])
    (3, 4)

    >>> find_two_unique_numbers([4,5,6,7,4,5])
    (6, 7)

    >>> find_two_unique_numbers([10,20,30,10,20,40])
    (30, 40)

    >>> find_two_unique_numbers([2,3])
    (2, 3)

    >>> find_two_unique_numbers([])
    Traceback (most recent call last):
        ...
    ValueError: input list must not be empty
    >>> find_two_unique_numbers([1, 'a', 1])
    Traceback (most recent call last):
        ...
    TypeError: all elements must be integers
    """

    if not arr:
        raise ValueError("input list must not be empty")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("all elements must be integers")

    xor_result = 0
    for number in arr:
        xor_result ^= number

    righmost_bit = xor_result & -xor_result

    num1 = 0
    num2 = 0

    for number in arr:
        if number & righmost_bit:
            num1 ^= number
        else:
            num2 ^= number
    a, b = sorted((num1, num2))
    return a, b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
