"""
Gcd of N Numbers
Reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
"""

from collections import Counter


def get_factors(number: int, factors: Counter | None = None, factor: int = 2) -> Counter:
    """
    this is a reccursive function for get all factors of number
    >>> get_factors(45)
    Counter({3: 2, 5: 1})
    >>> get_factors(2520)
    Counter({2: 3, 3: 2, 5: 1, 7: 1})
    >>> get_factors(23)
    Counter({23: 1})
    
    factor can be all numbers from 2 to number that we check if number % factor == 0
    if it is equal to zero, we check again with number // factor
    else we increase factor by one
    """

    if not isinstance(number, int):
        raise TypeError("number must be integer")

    if factors is None: 
        # first call of get factors and so there are no founded factors 
        factors = Counter()

    if number == factor: # break condition
        # all numbers are factors of itself
        factors[factor] += 1
        return factors

    if number % factor > 0:
        # if it is grater than zero
        # so it is not a factor of number and we check next number
        return get_factors(number, factors, factor + 1)

    factors[factor] += 1
    # else we update factors (that is Counter(dict-like) type) and check again
    return get_factors(number // factor, factors, factor)


def get_greatest_common_divisor(*numbers: int) -> int:
    """
    get gcd of n numbers:
    >>> get_greatest_common_divisor(18, 45)
    9
    >>> get_greatest_common_divisor(23, 37)
    1
    >>> get_greatest_common_divisor(2520, 8350)
    10
    """
    # we just need factors, not numbers itself
    data = [get_factors(number) for number in numbers]
    same_factors: Counter = data[0]
    for d in data[1:]:
        same_factors = same_factors & d 
        # get common factor between all
        # `&` return common elements with smaller value (for Counter type)
    
    # now, same_factors is something like {2: 2, 3: 4} that means 2 * 2 * 3 * 3 * 3 * 3
    mult = 1
    # power each factor and multiply
    # for {2: 2, 3: 4}, it is [4, 81] and then 324
    for m in [factor ** same_factors[factor] for factor in same_factors]:
        mult *= m
    return mult


if __name__ == "__main__":
    print(get_greatest_common_divisor(18, 45))  # 9
