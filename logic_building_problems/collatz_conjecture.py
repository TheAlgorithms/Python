"""
The Collatz Conjecture (3n + 1 Problem)
https://en.wikipedia.org/wiki/Collatz_conjecture
"""


def collatz_sequence(start_number: int) -> list[int]:
    """
    Generates the Collatz sequence for a given starting number.
    >>> collatz_sequence(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(1)
    [1]
    """
    if start_number <= 0:
        return []

    number = start_number
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    try:
        num = int(input("Enter a positive integer to start the Collatz sequence: "))
        if num > 0:
            print(f"Sequence: {collatz_sequence(num)}")
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
