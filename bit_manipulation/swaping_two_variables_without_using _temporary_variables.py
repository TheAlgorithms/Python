def xor_swap(a: int, b: int) -> (int, int):
    """
    Swap two integers using bitwise XOR
    without using a temporary variable.

    This algorithm utilizes the properties
    of the bitwise XOR operation to swap the values
    of two integers `a` and `b` without
    the use of a temporary variable. XOR swap is a
    rarely used trick but showcases the power
    of bit manipulation for efficient operations
    at the hardware level.

    The steps involved are:
    1. `a = a ^ b`
    2. `b = a ^ b` (Now `b` holds the original value of `a`)
    3. `a = a ^ b` (Now `a` holds the original value of `b`)

    Although this technique can swap variables
    without extra space, it is generally not
    recommended in production code because it is
    less readable than using a temporary variable.

    Args:
        a (int): The first integer to be swapped.
        b (int): The second integer to be swapped.

    Returns:
        (int, int): The swapped values of `a` and `b`.

    Raises:
        None

    Example:
        >>> xor_swap(5, 10)
        (10, 5)
        >>> xor_swap(0, 100)
        (100, 0)
        >>> xor_swap(-3, 9)
        (9, -3)

    Notes:
        - Swapping using XOR can lead to confusion and
        should generally be avoided in
        favor of more readable methods.
        - This algorithm does not work if both `a` and `b`
        refer to the same variable.

    """
    if a == b:
        print("Both values are the same; no swap needed.")
        return a, b

    # print(f"Original a = {a}, b = {b}")
    a = a ^ b  # Step 1
    b = a ^ b  # Step 2: Now b is the original value of a
    a = a ^ b  # Step 3: Now a is the original value of b
    # print(f"Swapped a = {a}, b = {b}")
    return a, b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(xor_swap(5, 10))  # (10, 5)
    print(xor_swap(0, 100))  # (100, 0)
    print(xor_swap(-3, 9))  # (9, -3)
