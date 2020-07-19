#!/usr/bin/env python

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


def solution(m):
    """ Returns the number under n that generates the longest Collatz sequence.

    >>> solution(1000000)
    {'counter': 525, 'largest_number': 837799}
    >>> solution(200)
    {'counter': 125, 'largest_number': 171}
    >>> solution(5000)
    {'counter': 238, 'largest_number': 3711}
    >>> solution(15000)
    {'counter': 276, 'largest_number': 13255}
    """
    # we are going to avoid repeat computations by creating a knowledge base
    # where we store the length of all collatz chains we calculated so far

    knowledge = {1: 1}

    # a single step in a collatz chain
    def collatz(n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    # calculates a collatz chain of a certain number this calculation is halted
    # whenever we find a key with a know collatz chain in our knowledge base
    def calculateChain(n):
        entries = []
        while n not in knowledge:
            entries.append(n)
            n = collatz(n)
        chainSize = knowledge[n]
        for i in entries[::-1]:
            chainSize += 1
            knowledge[i] = chainSize

    maxChain = {
        "counter": 1,
        "largest_number": 1
    }
    for i in range(1, m + 1):
        calculateChain(i)
        if maxChain["counter"] < knowledge[i]:
            maxChain = {
                "counter": knowledge[i],
                "largest_number": i
            }

    return maxChain


if __name__ == "__main__":
    print("calculate the number with the longest collatz chain in the range between 1 and the following number:")
    inputNumber = int(input().strip())
    number, chainLength = solution(inputNumber)
    print(f"the maximum collatz chain of all numbers between 1 and {inputNumber} is {chainLength}, starting with the number {number}")

