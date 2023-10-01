"""
GCD of N Numbers
Reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
"""

from collections import Counter


def get_factors(
    number: int, factors: Counter | None = None, factor: int = 2
) -> Counter:
    """
    This is a recursive function to get all factors of a number.

    :param number: The number to find factors for.
    :param factors: A Counter object to store factors.
    :param factor: The current factor to check.
    :return: A Counter object containing the factors.
    :raises TypeError: If the number is not an integer or is less than or equal to zero.
    """

    if not isinstance(number, int) or number <= 0:
        raise TypeError("number must be an integer and greater than zero")

    factors = factors or Counter()

    if number == factor:  # Break condition
        # All numbers are factors of itself
        factors[factor] += 1
        return factors

    if number % factor > 0:
        # If it is greater than zero, it is not a factor of the number,
        # so we check the next number
        return get_factors(number, factors, factor + 1)

    factors[factor] += 1
    # Otherwise, we update factors and check again
    return get_factors(number // factor, factors, factor)


def get_greatest_common_divisor(*numbers: int) -> int:
    """
    Get the greatest common divisor (GCD) of n numbers.

    :param numbers: A variable number of integers to find the GCD for.
    :return: The GCD of the input numbers.
    :raises Exception: If any input number is not an integer or is less than or equal to zero.
    """

    # We just need factors, not numbers themselves
    try:
        same_factors, *factors = map(get_factors, numbers)
    except TypeError as e:
        raise Exception("numbers must be integer and greater than zero") from e

    for factor in factors:
        same_factors &= factor
        # Get the common factor between all using bitwise AND

    # Now, same_factors is something like {2: 2, 3: 4}, which means 2 * 2 * 3 * 3 * 3 * 3
    mult = 1
    # Power each factor and multiply
    # For {2: 2, 3: 4}, it is [4, 81] and then 324
    for m in [factor**power for factor, power in same_factors.items()]:
        mult *= m
    return mult


if __name__ == "__main__":
    print(get_greatest_common_divisor(18, 45))  # 9
