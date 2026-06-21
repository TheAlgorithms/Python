"""
Next Prime Number -- https://en.wikipedia.org/wiki/Prime_number

In the ancient city of Numeria,
legends speak of an oracle whose whispers
could bend the very fabric of mathematics.
Travelers from distant lands would bring her a number,
and in return, she would reveal its future:
the very next prime number.
Your task is to embody the oracle's wisdom.
You will be given a number.
You must find the smallest prime number
that is strictly greater than it.
"""


def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(19)
    True
    >>> is_prime(1)
    False
    >>> is_prime(-7)
    False
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    factor = 5
    while factor * factor <= number:
        if number % factor == 0 or number % (factor + 2) == 0:
            return False
        factor += 6
    return True


def next_prime(number: int) -> int:
    """
    Find the smallest prime number strictly greater than the given number.

    >>> next_prime(2)
    3
    >>> next_prime(7)
    11
    >>> next_prime(14)
    17
    >>> next_prime(0)
    2
    >>> next_prime(-10)
    2
    """
    if not isinstance(number, int):
        raise ValueError("next_prime() only accepts integral values")

    candidate = number + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        n = int(input("Enter an integer: ").strip() or 0)
        print(f"The next prime number after {n} is {next_prime(n)}")
    except ValueError:
        print("Please enter a valid integer.")
