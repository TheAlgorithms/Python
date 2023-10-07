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
def nth_prime(n: int) -> Optional[int]:
    """
    Returns the nth prime number.

    Args:
        n (int): The position of the prime number to find.

    Returns:
        int: The nth prime number, or None if n is less than 1.
    """
    if n < 1:
        return None

    prime_counter = 2                # Initialize prime counter to 2, the first prime
    for num in range(3, n ** 2, 2):  # Loop through odd numbers starting from 3
        divisor = 1                  # Initialize divisor to 1
        while divisor * divisor < num:  # Loop through divisors up to sqrt of current num
            divisor += 2             # Increment divisor by 2 since even numbers are not prime
            if num % divisor == 0:   # If current num is divisible by divisor, it's not prime
                break                # Exit the loop
        else:                          # If loop completes without finding a divisor, current num is prime
            prime_counter += 1         # Increment prime counter
        if prime_counter == n:         # If we've found the nth prime number
            return num                 # Return the current num

# Function to find the solution for Project Euler Problem 7
def solution() -> int:
    """
    Returns the 10001st prime number.
    """
    result = nth_prime(10001)      # Find the 10001st prime number
    
    if result is not None:
        return result
    else:
        return -1  # Return -1 to indicate an error if input is invalid

if __name__ == "__main__":
    print(f"{solution() = }")  # Print the result of the solution function
