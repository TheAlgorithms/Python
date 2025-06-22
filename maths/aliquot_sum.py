from __future__ import annotations

import doctest
from typing import overload


@overload
def aliquot_sum(input_num: int) -> int: ...
@overload
def aliquot_sum(input_num: int, return_factors: bool) -> tuple[int, list[int]]: ...


def aliquot_sum(
    input_num: int, return_factors: bool = False
) -> int | tuple[int, list[int]]:
    """
    Calculates the aliquot sum of a positive integer.
    The aliquot sum is the sum of all proper divisors of a number.

    Args:
        input_num: Positive integer
        return_factors: If True, returns (sum, sorted_factor_list)

    Returns:
        Aliquot sum or (sum, factors) if return_factors=True

    Raises:
        TypeError: If input not integer
        ValueError: If input not positive

    Examples:
        >>> aliquot_sum(15)
        9
        >>> aliquot_sum(15, True)
        (9, [1, 3, 5])
    """
    # Validate input
    if not isinstance(input_num, int):
        raise TypeError("Input must be an integer")
    if input_num <= 0:
        raise ValueError("Input must be positive integer")

    # Special case: 1 has no proper divisors
    if input_num == 1:
        return (0, []) if return_factors else 0

    # Initialize factors and total
    factors = [1]
    total = 1
    sqrt_num = int(input_num**0.5)

    # Find factors efficiently
    for divisor in range(2, sqrt_num + 1):
        if input_num % divisor == 0:
            factors.append(divisor)
            total += divisor
            complement = input_num // divisor
            if complement != divisor:
                factors.append(complement)
                total += complement

    factors.sort()
    return (total, factors) if return_factors else total


def classify_number(n: int) -> str:
    """
    Classifies number based on aliquot sum:
    - Perfect: sum = number
    - Abundant: sum > number
    - Deficient: sum < number

    Examples:
        >>> classify_number(6)
        'Perfect'
        >>> classify_number(12)
        'Abundant'
    """
    if n <= 0:
        raise ValueError("Input must be positive integer")
    if n == 1:
        return "Deficient"

    s = aliquot_sum(n)  # Always returns int
    if s == n:
        return "Perfect"
    return "Abundant" if s > n else "Deficient"


if __name__ == "__main__":
    doctest.testmod()

    print("Aliquot sum of 28:", aliquot_sum(28))

    # Handle tuple return explicitly
    result = aliquot_sum(28, True)
    if isinstance(result, tuple):
        print("Factors of 28:", result[1])

    print("Classification of 28:", classify_number(28))

    # Large number test
    try:
        print("Aliquot sum for 10^9:", aliquot_sum(10**9))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
