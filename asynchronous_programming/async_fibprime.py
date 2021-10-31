import doctest
from asyncio import gather, run
from math import sqrt
from async_lru import alru_cache


@alru_cache(maxsize=256)
async def fib(digit: int) -> int:

    """
    >>> run(fib(10))
    55
    >>> run(fib(20))
    6765
    >>> run(fib(1))
    1

    """

    if digit == 0:
        return 0
    elif digit == 1:
        return 1
    else:
        return await fib(digit - 1) + await fib(digit - 2)


async def is_prime(digit: int) -> bool:

    """
    >>> run(is_prime(70))
    False
    >>> run(is_prime(2))
    True

    """

    prime_flag = 0

    if digit <= 1:
        return False

    for i in range(2, int(sqrt(digit)) + 1):
        if digit % i == 0:
            prime_flag = 1
            break
    return prime_flag == 0


async def main(input_n: int) -> None:
    """
    >>> run(main(10))
    10th fibo series is 55
    10 is not a prime number

    >>> run(main(20))
    20th fibo series is 6765
    20 is not a prime number

    """

    try:
        ret_fib, ret_prime = (
            await gather(fib(input_n), is_prime(input_n))
            if input_n >= 0
            else (None, await is_prime(input_n))
        )
        print(f"{input_n}th fibo series is", ret_fib) if ret_fib else print(
            "Invalid input"
        )

        print(f"{input_n} is a prime number") if ret_prime else print(
            f"{input_n} is not a prime number"
        )
    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    try:
        n = int(input("Enter a number: "))
        run(main(n))
    except ValueError:
        print("Input must an integer!")
