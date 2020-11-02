"""
    Project Euler Problem 074: https://projecteuler.net/problem=74

    Starting from any positive integer number
    it is possible to attain another one summing the factorial of its digits.

    Repeating this step, we can build chains of numbers.
    It is not difficult to prove that EVERY starting number
    will eventually get stuck in a loop.

    The request is to find how many numbers less than one million
    produce a chain with exactly 60 non repeating items.

    Solution approach:
    This solution simply consists in a loop that generates
    the chains of non repeating items.
    The generation of the chain stops before a repeating item
    or if the size of the chain is greater then the desired one.
    After generating each chain, the length is checked and the counter increases.
"""


def factorial(a: int) -> int:
    """Returns the factorial of the input a
    >>> factorial(5)
    120

    >>> factorial(6)
    720

    >>> factorial(0)
    1
    """

    # The factorial function is not defined for negative numbers
    if a < 0:
        raise ValueError("Invalid negative input!", a)

    # The case of 0! is handled separately
    if a == 0:
        return 1
    else:
        # use a temporary support variable to store the computation
        temporary_computation = 1

        while a > 0:
            temporary_computation *= a
            a -= 1

        return temporary_computation


def factorial_sum(a: int) -> int:
    """Function to perform the sum of the factorial
    of all the digits in a

    >>> factorial_sum(69)
    363600
    """

    # Prepare a variable to hold the computation
    fact_sum = 0

    """ Convert a in string to iterate on its digits
        convert the digit back into an int
        and add its factorial to fact_sum.
    """
    for i in str(a):
        fact_sum += factorial(int(i))

    return fact_sum


def solution(chain_length: int = 60, number_limit: int = 1000000) -> int:
    """Returns the number of numbers that produce
        chains with exactly 60 non repeating elements.
    >>> solution(60,1000000)
    402
    >>> solution(15,1000000)
    17800
    """

    # the counter for the chains with the exact desired length
    chain_counter = 0

    for i in range(1, number_limit + 1):

        # The temporary list will contain the elements of the chain
        chain_list = [i]

        # The new element of the chain
        new_chain_element = factorial_sum(chain_list[-1])

        """ Stop computing the chain when you find a repeating item
            or the length it greater then the desired one.
        """
        while not (new_chain_element in chain_list) and (
            len(chain_list) <= chain_length
        ):
            chain_list += [new_chain_element]

            new_chain_element = factorial_sum(chain_list[-1])

        """ If the while exited because the chain list contains the exact amount of elements
            increase the counter
        """
        chain_counter += len(chain_list) == chain_length

    return chain_counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution()}")
