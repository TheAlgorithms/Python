from typing import Union
from asyncio import gather, run
from math import sqrt
import doctest


async def fib(digit: int) -> Union[int, str]:

    """
    >>> run(fib(10))
    55
    >>> run(fib(20))
    6765
    >>> run(fib(-7))
    'Number must be a positive integer!'
    >>> run(fib(1))
    1

    """

    if digit < 0:
        return "Number must be a positive integer!"
    elif digit == 0:
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


async def main() -> None:
    try:
        put_num = int(input("Enter a number: "))
        ret_fib, ret_prime = await gather(fib(put_num), is_prime(put_num))
        print(f"{put_num}th fibo series is", ret_fib)

        print(f"{put_num} is a prime number") if ret_prime else print(
            f"{put_num} is not a prime number"
        )
    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    run(main())
