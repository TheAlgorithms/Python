"""
Project Euler Problem 7: https://projecteuler.net/problem=7

10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
can see that the 6th prime is 13.

What is the 10001st prime number?

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""


# Function to find the nth prime number
def nth_prime(n: int) -> [int]:
    """
    Returns the nth prime number.

    Args:
        n (int): The position of the prime number to find.

    Returns:
        int: The nth prime number, or None if n is less than 1.
    """
    if n < 1:
        return None

    prime_counter = (
        2  # Initialize the prime counter to 2 since 2 is the first prime 
    )
    for num in range(3, n**2, 2):  # Loop through odd numbers starting from 3
        divisor = 1  # Initialize the divisor to 1
        while (
            divisor * divisor < num
        ):  # Loop through divisors up to the square root of the current number
            divisor += 2  
            if (
                num % divisor == 0
            ):  # If the current number is divisible by the divisor
                break  # Exit the loop
        else:  
            prime_counter += 1  # Increment the prime counter
        if prime_counter == n:  # If we have found the nth prime number
            return num  # Return the current number


# Function to find the solution for Project Euler Problem 7
def solution() -> int:
    """
    Returns the 10001st prime number.
    """
    result = nth_prime(10001)  # Find the 10001st prime number

    if result is not None:
        return result
    else:
        return -1  # Return -1 to indicate an error if input is invalid


if __name__ == "__main__":
    print(f"{solution() = }")  # Print the result of the solution function
