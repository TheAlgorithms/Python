"""
Kaprekar's Constant (6174) - also known as Kaprekar's Routine

Kaprekar's constant is a special number discovered by Indian mathematician
D. R. Kaprekar in 1949. It is notable for the following property:

1. Take any four-digit number with at least two different digits (leading zeros allowed)
2. Arrange the digits in descending order to form the largest possible number
3. Arrange the digits in ascending order to form the smallest possible number
4. Subtract the smaller number from the larger number
5. Repeat the process with the result

This process will always reach 6174 in at most 7 iterations, and once 6174 is
reached, the process will continue to yield 6174.

Example:
    3524 -> 5432 - 2345 = 3087
    3087 -> 8730 - 0378 = 8352
    8352 -> 8532 - 2358 = 6174
    6174 -> 7641 - 1467 = 6174 (repeats)

Reference: https://en.wikipedia.org/wiki/6174_(number)
OEIS: https://oeis.org/A099009
"""


def kaprekar_routine(number: int) -> int:
    """
    Perform one iteration of Kaprekar's routine.

    Args:
        number: A 4-digit number (0-9999)

    Returns:
        The result of one Kaprekar iteration

    >>> kaprekar_routine(3524)
    3087
    >>> kaprekar_routine(3087)
    8352
    >>> kaprekar_routine(8352)
    6174
    >>> kaprekar_routine(6174)
    6174
    >>> kaprekar_routine(1)
    999
    >>> kaprekar_routine(1111)
    0
    """
    if not isinstance(number, int) or number < 0 or number > 9999:
        msg = f"Input must be a non-negative integer between 0 and 9999, got {number}"
        raise ValueError(msg)

    # Convert to 4-digit string with leading zeros
    digits = str(number).zfill(4)

    # Check if all digits are the same (repdigit)
    if len(set(digits)) == 1:
        return 0

    # Sort digits in descending and ascending order
    descending = int("".join(sorted(digits, reverse=True)))
    ascending = int("".join(sorted(digits)))

    return descending - ascending


def kaprekar_constant(number: int, max_iterations: int = 7) -> tuple[int, list[int]]:
    """
    Apply Kaprekar's routine until reaching the constant 6174 or max iterations.

    Args:
        number: A 4-digit number (0-9999)
        max_iterations: Maximum number of iterations to perform (default: 7)

    Returns:
        A tuple containing:
        - The number of iterations taken to reach 6174 (or -1 if not reached)
        - A list of all intermediate results

    >>> kaprekar_constant(3524)
    (3, [3524, 3087, 8352, 6174])
    >>> kaprekar_constant(6174)
    (0, [6174])
    >>> kaprekar_constant(1234)
    (3, [1234, 3087, 8352, 6174])
    >>> kaprekar_constant(1111)
    (-1, [1111, 0])
    >>> kaprekar_constant(495)
    (4, [495, 9081, 9621, 8352, 6174])
    >>> kaprekar_constant(9998)
    (5, [9998, 999, 8991, 8082, 8532, 6174])
    """
    if not isinstance(number, int) or number < 0 or number > 9999:
        msg = f"Input must be a non-negative integer between 0 and 9999, got {number}"
        raise ValueError(msg)

    if not isinstance(max_iterations, int) or max_iterations < 1:
        msg = f"max_iterations must be a positive integer, got {max_iterations}"
        raise ValueError(msg)

    sequence = [number]
    current = number

    # If already at Kaprekar's constant
    if current == 6174:
        return (0, sequence)

    for iteration in range(max_iterations):
        current = kaprekar_routine(current)
        sequence.append(current)

        # Check if we've reached the constant
        if current == 6174:
            return (iteration + 1, sequence)

        # Check if we've reached a repdigit (all same digits) which gives 0
        if current == 0:
            return (-1, sequence)

    # Did not reach 6174 within max_iterations
    return (-1, sequence)


def is_kaprekar_valid(number: int) -> bool:
    """
    Check if a number is valid for Kaprekar's routine.
    A number is valid if it has at least two different digits.

    Args:
        number: A 4-digit number (0-9999)

    Returns:
        True if the number is valid for Kaprekar's routine, False otherwise

    >>> is_kaprekar_valid(3524)
    True
    >>> is_kaprekar_valid(1111)
    False
    >>> is_kaprekar_valid(1000)
    True
    >>> is_kaprekar_valid(1)
    True
    >>> is_kaprekar_valid(6174)
    True
    """
    if not isinstance(number, int) or number < 0 or number > 9999:
        msg = f"Input must be a non-negative integer between 0 and 9999, got {number}"
        raise ValueError(msg)

    # Convert to 4-digit string with leading zeros
    digits = str(number).zfill(4)

    # Check if at least two different digits exist
    return len(set(digits)) > 1


def main() -> None:
    """
    Demonstrate Kaprekar's constant with user input and examples.
    """
    print("Kaprekar's Constant (6174) - Demonstration\n")
    print("=" * 50)

    # Example demonstrations
    examples = [3524, 1234, 6174, 9998, 1111, 5]

    for num in examples:
        print(f"\nStarting number: {num:04d}")
        if not is_kaprekar_valid(num):
            print("  ❌ Invalid: All digits are the same (repdigit)")
            continue

        iterations, sequence = kaprekar_constant(num)
        if iterations == -1:
            print(f"  ❌ Did not reach 6174. Sequence: {sequence}")
        elif iterations == 0:
            print("  ✓ Already at Kaprekar's constant!")
        else:
            print(f"  ✓ Reached 6174 in {iterations} iteration(s)")
            print(f"  Sequence: {' -> '.join(str(n) for n in sequence)}")

    # Interactive mode
    print("\n" + "=" * 50)
    print("\nTry your own number (0-9999):")
    try:
        user_input = int(input("Enter a 4-digit number: "))
        if 0 <= user_input <= 9999:
            if not is_kaprekar_valid(user_input):
                print("Invalid: All digits are the same!")
            else:
                iterations, sequence = kaprekar_constant(user_input)
                print(f"\nSequence: {' -> '.join(str(n) for n in sequence)}")
                if iterations != -1:
                    print(f"Reached 6174 in {iterations} iteration(s)!")
        else:
            print("Number must be between 0 and 9999")
    except (ValueError, EOFError):
        print("Invalid input or no input provided")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
