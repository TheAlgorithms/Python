"""
Project Euler Problem 074: https://projecteuler.net/problem=74

The number 145 is well known for the property that the sum of the factorial of its
digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that
link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a
loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?

Solution approach:
This solution simply consists in a loop that generates the chains of non repeating
items using the cached sizes of the previous chains.
The generation of the chain stops before a repeating item or if the size of the chain
is greater then the desired one.
After generating each chain, the length is checked and the counter increases.
"""
from math import factorial

DIGIT_FACTORIAL: dict[str, int] = {str(digit): factorial(digit) for digit in range(10)}


def digit_factorial_sum(number: int) -> int:
    """
    Function to perform the sum of the factorial of all the digits in number

    >>> digit_factorial_sum(69.0)
    Traceback (most recent call last):
        ...
    TypeError: Parameter number must be int

    >>> digit_factorial_sum(-1)
    Traceback (most recent call last):
        ...
    ValueError: Parameter number must be greater than or equal to 0

    >>> digit_factorial_sum(0)
    1

    >>> digit_factorial_sum(69)
    363600
    """
    if not isinstance(number, int):
        raise TypeError("Parameter number must be int")

    if number < 0:
        raise ValueError("Parameter number must be greater than or equal to 0")

    # Converts number in string to iterate on its digits and adds its factorial.
    return sum(DIGIT_FACTORIAL[digit] for digit in str(number))


def solution(chain_length: int = 60, number_limit: int = 1000000) -> int:
    """
    Returns the number of numbers below number_limit that produce chains with exactly
    chain_length non repeating elements.

    >>> solution(10.0, 1000)
    Traceback (most recent call last):
        ...
    TypeError: Parameters chain_length and number_limit must be int

    >>> solution(10, 1000.0)
    Traceback (most recent call last):
        ...
    TypeError: Parameters chain_length and number_limit must be int

    >>> solution(0, 1000)
    Traceback (most recent call last):
        ...
    ValueError: Parameters chain_length and number_limit must be greater than 0

    >>> solution(10, 0)
    Traceback (most recent call last):
        ...
    ValueError: Parameters chain_length and number_limit must be greater than 0

    >>> solution(10, 1000)
    26
    """

    if not isinstance(chain_length, int) or not isinstance(number_limit, int):
        raise TypeError("Parameters chain_length and number_limit must be int")

    if chain_length <= 0 or number_limit <= 0:
        raise ValueError(
            "Parameters chain_length and number_limit must be greater than 0"
        )

    # the counter for the chains with the exact desired length
    chains_counter = 0
    # the cached sizes of the previous chains
    chain_sets_lengths: dict[int, int] = {}

    for start_chain_element in range(1, number_limit):

        # The temporary set will contain the elements of the chain
        chain_set = set()
        chain_set_length = 0

        # Stop computing the chain when you find a cached size, a repeating item or the
        # length is greater then the desired one.
        chain_element = start_chain_element
        while (
            chain_element not in chain_sets_lengths
            and chain_element not in chain_set
            and chain_set_length <= chain_length
        ):
            chain_set.add(chain_element)
            chain_set_length += 1
            chain_element = digit_factorial_sum(chain_element)

        if chain_element in chain_sets_lengths:
            chain_set_length += chain_sets_lengths[chain_element]

        chain_sets_lengths[start_chain_element] = chain_set_length

        # If chain contains the exact amount of elements increase the counter
        if chain_set_length == chain_length:
            chains_counter += 1

    return chains_counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution()}")
