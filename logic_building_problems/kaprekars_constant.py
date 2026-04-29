"""
Kaprekar's Constant (6174)
https://en.wikipedia.org/wiki/6174_(number)
"""

KAPREKARS_CONSTANT = 6174


def kaprekar_routine(four_digit_number: int) -> list[int]:
    """
    Performs the Kaprekar routine and returns the sequence of numbers.
    >>> kaprekar_routine(3524)
    [3524, 3087, 8352, 6174]
    """
    if not 1000 <= four_digit_number <= 9999:
        raise ValueError("Input must be a four-digit number.")
    if len(set(str(four_digit_number).zfill(4))) < 2:
        raise ValueError("Input must have at least two different digits.")

    number = four_digit_number
    sequence = [number]
    while number != KAPREKARS_CONSTANT:
        s_num = str(number).zfill(4)
        desc_str = "".join(sorted(s_num, reverse=True))
        asc_str = "".join(sorted(s_num))
        number = int(desc_str) - int(asc_str)
        sequence.append(number)
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    try:
        num = int(
            input("Enter a 4-digit number (with at least two different digits): ")
        )
        result_sequence = kaprekar_routine(num)
        print(f"Sequence: {' -> '.join(map(str, result_sequence))}")
    except ValueError as e:
        print(f"Error: {e}")
