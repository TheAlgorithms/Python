"""
From: https://en.wikipedia.org/wiki/Amicable_numbers
Amicable numbers are two different numbers related in such a way that the sum of the proper divisors of each is equal to the other number.

>>> amicable_numbers(60,84)
False
>>> amicable_numbers(220,284)
True
>>> amicable_numbers(-10,24)
False
"""


def amicable_numbers(first_number, second_number) -> bool:
    if first_number <= 1 or second_number <= 1:
        return False
    first_number_proper_divisors = [
        i for i in range(1, first_number) if first_number % i == 0
    ]
    second_number_proper_divisors = [
        i for i in range(1, second_number) if second_number % i == 0
    ]
    return (
        sum(first_number_proper_divisors) == second_number
        and sum(second_number_proper_divisors) == first_number
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
