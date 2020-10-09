"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


def solution(limit: int = 1000000) -> int:
    """
    Return the prime below 10^6 that can be written as the sum of the most
    consecutive primes.
    """
    prime_set = set(range(3, limit, 2))
    prime_set.add(2)
    for p in range(3, limit, 2):
        if p not in prime_set:
            continue
        prime_set.difference_update(set(range(p * p, limit, p)))

    prime_list = sorted(prime_set)

    answer = 0
    longest_chain = 2

    for first_index in range(len(prime_list) - 1):
        chain_length = 3 if first_index else 2
        total = sum(prime_list[first_index : first_index + chain_length])
        if total >= limit:
            break
        while first_index + chain_length < len(prime_list) and total < limit:
            if total in prime_set and chain_length > longest_chain:
                answer = total
                longest_chain = chain_length
            total += prime_list[first_index + chain_length]
            total += prime_list[first_index + chain_length + 1]
            chain_length += 2

    return answer


if __name__ == "__main__":
    print(solution())
