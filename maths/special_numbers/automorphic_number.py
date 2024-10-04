def is_automorphic_number(number: int, verbose: bool = False) -> bool:
    """
    This function checks if a given number is an automorphic number.

    Returns:
    bool: True if the number is automorphic, False otherwise.

    Raises:
    TypeError: If the input number is not an integer.
    ValueError: If the input number is negative.
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 0:
        msg = f"Input value of [number={number}] must be a non-negative integer"
        raise ValueError(msg)
    number_square = number * number
    if verbose:
        print(f"Square of {number}: {number_square}")
    while number > 0:
        if number % 10 != number_square % 10:
            if verbose:
                print(f"{number} is not an automorphic number")
            return False
        number //= 10
        number_square //= 10
    if verbose:
        print(f"{number} is an automorphic number")
    return True


def find_automorphic_numbers(n: int) -> list:
    """
    This function finds all automorphic numbers up to a given number.

    Args:
    n (int): The upper limit.

    Returns:
    list: A list of automorphic numbers up to n.
    """
    automorphic_numbers = []
    for i in range(n + 1):
        if is_automorphic_number(i):
            automorphic_numbers.append(i)
    return automorphic_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage:
    print(is_automorphic_number(25, verbose=True))
    print(find_automorphic_numbers(100))
