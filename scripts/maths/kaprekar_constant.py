def kaprekar_routine(number: int) -> int:
    """
    Find steps to Kaprekar constant (6174) bro.
    Link: https://wikipedia.org

    >>> kaprekar_routine(3524)
    3
    >>> kaprekar_routine(6174)
    0
    """

    # Checking if the number is 4 digits, throwing an error if not bro
    if not (1000 <= number <= 9999):
        raise ValueError("The number must be 4 digits bro!")

    # If someone enters all same digits like 1111, loop breaks. Blocking it here
    if len(set(str(number))) < 2:
        raise ValueError(
            "Digits cannot be all the same bro, make at least two different!"
        )

    kaprekar_target = 6174
    steps = 0

    # We are here until the number becomes 6174 bro, loop keeps spinning
    while number != kaprekar_target:
        # Padding the number to 4 digits and making it a string bro
        digits = f"{number:04d}"

        # Sorting digits from biggest to smallest and joining them
        descending = int("".join(sorted(digits, reverse=True)))

        # Sorting digits from smallest to biggest and joining them
        ascending = int("".join(sorted(digits)))

        # Subtracting smallest from biggest, finding new number and increasing steps bro
        number = descending - ascending
        steps += 1

        # Infinite loop protection just in case we break something, spins 7 times max
        if steps > 7:
            break

    return steps


if __name__ == "__main__":
    import doctest

    # Running the test engine that the bots are checking
    doctest.testmod()

    # Just a small example here to test it for myself
    print(f"Our number locked in exactly {kaprekar_routine(3524)} steps bro!")
