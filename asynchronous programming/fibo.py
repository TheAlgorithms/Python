from typing import Union
from async_lru import alru_cache
from asyncio import gather, run
from math import sqrt

@alru_cache(maxsize=256)  # using memoization to speed up the process
async def fib(n: int) -> Union[int, str]:
    if n < 0:
        return "Number must be a positive integer!"
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (await fib(n-1) + await fib(n-2))
    
async def is_prime(n: int) -> bool:
    prime_flag = 0

    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    return (prime_flag == 0)
        


async def main():
    try:
        put_num=int(input("Enter a number: "))
        ret_fib, ret_prime = await gather(fib(put_num), is_prime(put_num))
        print(f"{put_num}th fibo series is", ret_fib)
        
        print(f"{put_num} is a prime number") if ret_prime else print(f"{put_num} is not a prime number") 
    except ValueError:
        print("Invalid input!")
        
run(main())