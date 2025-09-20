def perfect_cube(n: int) -> bool:
    """
    Check if a number is a perfect cube or not.

    Note: This method uses floating point arithmetic which may be
    imprecise for very large numbers.

    >>> perfect_cube(27)
    True
    >>> perfect_cube(64)
    True
    >>> perfect_cube(4)
    False
    >>> perfect_cube(0)
    True
    >>> perfect_cube(1)
    True
    >>> perfect_cube(-8)  # Negative perfect cube
    True
    >>> perfect_cube(-9)  # Negative non-perfect cube
    False
    >>> perfect_cube(10**6)  # Large perfect cube (100^3)
    True
    >>> perfect_cube(10**6 + 1)  # Large non-perfect cube
    False
    """
    # Handle negative numbers
    if is_negative := n < 0:
        n = -n
    val = n ** (1 / 3)
    # Round to avoid floating point precision issues
    rounded_val = round(val)
    result = rounded_val * rounded_val * rounded_val == n

    # For negative numbers, we need to check if the cube root would be negative
    return result and not (is_negative and rounded_val == 0)


def perfect_cube_binary_search(n: int) -> bool:
    """
    Check if a number is a perfect cube or not using binary search.
    Time complexity : O(Log(n))
    Space complexity: O(1)

    >>> perfect_cube_binary_search(27)
    True
    >>> perfect_cube_binary_search(64)
    True
    >>> perfect_cube_binary_search(4)
    False
    >>> perfect_cube_binary_search(0)
    True
    >>> perfect_cube_binary_search(1)
    True
    >>> perfect_cube_binary_search(-8)  # Negative perfect cube
    True
    >>> perfect_cube_binary_search(-9)  # Negative non-perfect cube
    False
    >>> perfect_cube_binary_search(10**6)  # Large perfect cube (100^3)
    True
    >>> perfect_cube_binary_search(10**6 + 1)  # Large non-perfect cube
    False
    >>> perfect_cube_binary_search(10**18)  # Very large perfect cube (10^6)^3
    True
    >>> perfect_cube_binary_search(10**18 + 1)  # Very large non-perfect cube
    False
    >>> perfect_cube_binary_search(10**100)  # Extremely large number
    False
    >>> perfect_cube_binary_search(10**300)  # Extremely large perfect cube (10^100)^3
    True
    >>> perfect_cube_binary_search(10**300 + 1)  # Extremely large non-perfect cube
    False
    >>> perfect_cube_binary_search("a")
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    >>> perfect_cube_binary_search(0.1)
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    >>> perfect_cube_binary_search(None)
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    >>> perfect_cube_binary_search([])
    Traceback (most recent call last):
        ...
    TypeError: perfect_cube_binary_search() only accepts integers
    """
    if not isinstance(n, int):
        raise TypeError("perfect_cube_binary_search() only accepts integers")

    # Handle zero and negative numbers
    if n == 0:
        return True
    if n < 0:
        n = -n

    # Quick checks to eliminate obvious non-cubes
    # Check last three digits using modulo arithmetic
    # Only 0, 1, 8, 7, 4, 5, 6, 3, 2, 9 can be cubes mod 10
    # But for cubes, the pattern is more complex
    last_digit = n % 10
    if last_digit not in {0, 1, 8, 7, 4, 5, 6, 3, 2, 9}:
        return False

    # More refined check: cubes mod 7 can only be 0, 1, 6
    if n % 7 not in {0, 1, 6}:
        return False

    # More refined check: cubes mod 9 can only be 0, 1, 8
    if n % 9 not in {0, 1, 8}:
        return False

    # Estimate the cube root using logarithms for very large numbers
    # This gives us a much better initial right bound
    if n > 10**18:
        # For very large numbers, use logarithmic approximation
        # to get a reasonable upper bound
        log_n = len(str(n))  # Approximate log10(n)
        approx_root = 10 ** (log_n // 3)
        left = max(0, approx_root // 10)
        right = approx_root * 10
    else:
        # For smaller numbers, use the standard approach
        left, right = 0, n // 2 + 1

    # Binary search
    while left <= right:
        mid = (left + right) // 2
        # Avoid computing mid*mid*mid for very large mid values
        # by checking if mid is too large first
        if mid > 10**6 and mid * mid > n // mid:
            right = mid - 1
            continue

        cube = mid * mid * mid
        if cube == n:
            return True
        elif cube < n:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
