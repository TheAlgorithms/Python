"""
Algorithm to calculate the absolute age difference between two people.

Wikipedia: https://en.wikipedia.org/wiki/Chronological_age
"""


def age_difference(boy_age: int, girl_age: int) -> int:
    """
    Return the absolute age difference between two people.

    The function raises a ValueError if any of the ages is negative.

    >>> age_difference(22, 20)
    2
    >>> age_difference(20, 22)
    2
    >>> age_difference(30, 30)
    0
    >>> age_difference(-1, 5)
    Traceback (most recent call last):
        ...
    ValueError: Age cannot be negative.
    >>> age_difference(18, -2)
    Traceback (most recent call last):
        ...
    ValueError: Age cannot be negative.
    """
    if boy_age < 0 or girl_age < 0:
        raise ValueError("Age cannot be negative.")
    return abs(boy_age - girl_age)


if __name__ == "__main__":
    # Example usage (not required by TheAlgorithms, but for local testing)
    print(age_difference(22, 20))  # 2
    print(age_difference(20, 22))  # 2
    print(age_difference(30, 30))  # 0
