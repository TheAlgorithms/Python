def kaprekar_routine(number: int) -> int:
    """
    Calculates the number of steps required to reach Kaprekar's constant (6174).
    Link: https://en.wikipedia.org/wiki/6174

    >>> kaprekar_routine(3524)
    3
    >>> kaprekar_routine(6174)
    0
    """

    # Ensure the input is a 4-digit positive integer
    if not (1000 <= number <= 9999):
        raise ValueError("The number must be a 4-digit integer.")

    # Prevent repdigits (e.g., 1111) which result in zero and cause infinite loops
    if len(set(str(number))) < 2:
        raise ValueError("The number must contain at least two distinct digits.")

    kaprekar_target = 6174
    steps = 0

    # Iterate until the number reaches Kaprekar's constant
    while number != kaprekar_target:
        # Zero-pad the number to ensure a 4-digit string representation
        digits = f"{number:04d}"

        # Sort digits in descending and ascending order
        descending = int("".join(sorted(digits, reverse=True)))
        ascending = int("".join(sorted(digits)))

        # Subtract smaller number from larger number to get the next iteration
        number = descending - ascending
        steps += 1

        # Safety check: Kaprekar's routine always reaches 6174 in at most 7 steps
        if steps > 7:
            break

    return steps


if __name__ == "__main__":
    import doctest

    # Execute automated doctests
    doctest.testmod()

    # Sample execution
    print(f"Iterations required: {kaprekar_routine(3524)}")
