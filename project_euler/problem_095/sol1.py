"""
Project Euler Problem: https://projecteuler.net/problem=95

An amicable chain is a sequence of numbers where each number is the sum of the 
proper divisors of the previous one, and the chain eventually returns to the 
starting number. The problem is to find the smallest member of the longest 
amicable chain under a given limit.

In this implementation, we aim to identify all amicable chains and find the 
one with the maximum length, while also returning the smallest member of that 
chain.
"""

def sum_of_proper_divisors(n):
    """Calculate the sum of proper divisors of n."""
    if n < 2:
        return 0  # Proper divisors of 0 and 1 are none.
    total = 1  # Start with 1, since it is a proper divisor of any n > 1
    sqrt_n = int(n**0.5)  # Calculate the integer square root of n.

    # Loop through possible divisors from 2 to the square root of n
    for i in range(2, sqrt_n + 1):
        if n % i == 0:  # Check if i is a divisor of n
            total += i  # Add the divisor
            if i != n // i:  # Avoid adding the square root twice
                total += n // i  # Add the corresponding divisor (n/i)

    return total

def find_longest_amicable_chain(limit):
    """Find the smallest member of the longest amicable chain under a given limit."""
    sum_divisors = {}  # Dictionary to store the sum of proper divisors for each number
    for i in range(1, limit + 1):
        sum_divisors[i] = sum_of_proper_divisors(i)  # Calculate and store sum of proper divisors

    longest_chain = []  # To store the longest amicable chain found
    seen = {}  # Dictionary to track numbers already processed

    # Iterate through each number to find amicable chains
    for start in range(1, limit + 1):
        if start in seen:  # Skip if this number is already processed
            continue

        chain = []  # Initialize the current chain
        current = start  # Start with the current number
        while current <= limit and current not in chain:
            chain.append(current)  # Add the current number to the chain
            seen[current] = True  # Mark this number as seen
            current = sum_divisors.get(current, 0)  # Move to the next number in the chain

        # Check if we form a cycle and validate the chain
        if current in chain and current != start:
            cycle_start_index = chain.index(current)  # Find where the cycle starts
            if current in sum_divisors and sum_divisors[current] in chain:
                # This means we have a valid amicable chain
                chain = chain[cycle_start_index:]  # Take only the cycle part
                if len(chain) > len(longest_chain):
                    longest_chain = chain  # Update longest chain if this one is longer

    return min(longest_chain) if longest_chain else None  # Return the smallest member of the longest chain

def solution():
    """Return the smallest member of the longest amicable chain under one million."""
    return find_longest_amicable_chain(10**6)

if __name__ == "__main__":
    smallest_member = solution()  # Call the solution function
    print(smallest_member)  # Output the smallest member of the longest amicable chain
