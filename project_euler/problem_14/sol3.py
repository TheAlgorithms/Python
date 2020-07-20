from typing import Tuple

"""
Collatz conjecture: start with any positive integer n. Next term obtained from
the previous term as follows:
If the previous term is even, the next term is one half the previous term.
If the previous term is odd, the next term is 3 times the previous term plus 1.
The conjecture states the sequence will always reach 1 regardless of starting
n.
Problem Statement:
The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
"""

# we are going to avoid repeat computations by creating a knowledge base
# where we store the length of all collatz chains we calculated so far

knowledge = {1: 1}


# a single step in a collatz chain
def collatz(n: int) -> int:
    """ calculates a single step in a collatz chain

    >>> collatz(13)
    40
    >>> collatz(40)
    20
    >>> collatz(5)
    16
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def calculate_chain(n: int) -> None:
    """
    calculates a collatz chain of a certain number this calculation is halted
    whenever we find a key with a know collatz chain in our knowledge base

    >>> knowledge = {1: 1}
    >>> calculate_chain(13)
    >>> knowledge
    {1: 1, 2: 2, 4: 3, 8: 4, 16: 5, 5: 6, 10: 7, 20: 8, 40: 9, 13: 10}
    >>> calculate_chain(8)
    >>> knowledge
    {1: 1, 2: 2, 4: 3, 8: 4, 16: 5, 5: 6, 10: 7, 20: 8, 40: 9, 13: 10}
    >>> knowledge = {1: 1}
    >>> calculate_chain(12)
    >>> knowledge
    {1: 1, 2: 2, 4: 3, 8: 4, 16: 5, 5: 6, 10: 7, 3: 8, 6: 9, 12: 10}
    """
    entries = []
    while n not in knowledge:
        entries.append(n)
        n = collatz(n)
    chain_size = knowledge[n]
    for i in entries[::-1]:
        chain_size += 1
        knowledge[i] = chain_size


def solution(m: int) -> Tuple[int, int]:
    """ Returns the number under n that generates the longest Collatz sequence.

    >>> solution(1000000)
    (837799, 525)
    >>> solution(200)
    (171, 125)
    >>> solution(5000)
    (3711, 238)
    >>> solution(15000)
    (13255, 276)
    """
    max_chain = (1, 1)
    for i in range(1, m + 1):
        calculate_chain(i)
        # we can use knowledge[i] because calculate_chain
        # by definition already adds the key we specified to the
        # knowledge base
        if max_chain[1] < knowledge[i]:
            max_chain = (i, knowledge[i])

    return max_chain


if __name__ == "__main__":
    print("""
    calculate the number with the longest collatz chain
    in the range between 1 and the following number:
          """)
    input_number = int(input().strip())
    number, chain_length = solution(input_number)
    print(f"""
    the maximum collatz chain of all numbers between 1 and {input_number} is
    {chain_length}, starting with the number {number}
          """)
