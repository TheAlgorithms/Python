"""
Project Euler Problem 60: https://projecteuler.net/problem=60

Prime Pair Sets

Problem: The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this property.

Question: Find the lowest sum for a set of five primes for which
any two primes concatenate to produce another prime.

Explanation of the solution: the idea in finding a set of primes that satisfy the
concatenation condition is to build a graph of primes where a node would represent a
prime and an edge between two nodes would indicate that the two primes form a valid
pair. Hence, the solution to the problem can be computed more efficiently since
it does not require brute-forcing all possible combinations.
"""

from itertools import combinations


def sieve_of_eratosthenes(limit: int) -> set[int]:
    """Generate primes up to a limit using the Sieve of Eratosthenes and return them
        as a set.

    Parameters
    ----------
    limit : int
        The upper limit to generate primes up to.

    Returns
    ----------
    set[int]
        A set of prime numbers up to the limit.
    """
    sieve: list = [True] * (limit + 1)
    primes_set = set()
    for p in range(2, limit + 1):
        if sieve[p]:
            primes_set.add(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes_set


def is_prime(n: int) -> bool:
    """Checks whether a number is prime or not.

    Parameters
    ----------
    n : int
        The number to be checked.

    Returns
    ----------
    bool
        True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def valid_pair(p1: int, p2: int) -> bool:
    """Checks whether a pair of primes concatenated both ways is prime or not.

    Parameters
    ----------
    p1 : int
        The first prime number.
    p2 : int
        The second prime number.

    Returns
    ----------
    bool
        True if the pair is valid, False otherwise.
    """
    return is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))


def build_graph(prime_set: set[int]) -> dict[int, set[int]]:
    """Builds a graph of primes where each prime is a node and an edge exists
        between two primes if they form a valid pair.

    Parameters
    ----------
    prime_set : set[int]
        A set of prime numbers.

    Returns
    ----------
    dict[int, set[int]]
        A graph of primes.
    """
    graph: dict[int, set[int]] = {p: set() for p in prime_set}
    for p1, p2 in combinations(prime_set, 2):
        if valid_pair(p1, p2):
            graph[p1].add(p2)
            graph[p2].add(p1)
    return graph


def find_cliques(
    node: int, graph: dict[int, set[int]], clique: set[int], depth: int
) -> list[set[int]]:
    """The problem of finding a set of n primes that all satisfy
        the concatenation condition can be reduced to that of finding
        a clique of size n in the graph of primes.

    Parameters
    ----------
    node : int
        The node to be considered.
    graph : dict[int, set[int]]
        The graph of primes.
    clique : set[int]
        The set of primes that form a clique.
    depth : int
        The size of the clique.

    Returns
    ----------
    list[set[int]]
        A list of sets of primes that form cliques of size n.
    """
    if depth == 1:
        return [clique]
    cliques: list[set[int]] = []
    for neighbour in graph[node]:
        if all(neighbour in graph[member] for member in clique):
            cliques.extend(
                find_cliques(neighbour, graph, clique | {neighbour}, depth - 1)
            )
    return cliques


def solution(n: int = 5) -> int:
    """Aims at finding the lowest sum for a set of five primes for which any two primes
        concatenate to produce another prime.

    Parameters
    ----------
    n : int
        The size of the set of primes (5 by default)

    Returns
    ----------
    int
        The lowest sum for a set of five primes for which any two primes concatenate to
        produce another prime.

    >>> solution()
    26033
    """
    limit: int = 10000  # the limit is arbitrary but is sufficient for the problem
    prime_set: set[int] = sieve_of_eratosthenes(limit)
    prime_graph: dict[int, set[int]] = build_graph(prime_set)

    for prime in prime_set:
        cliques = find_cliques(prime, prime_graph, {prime}, depth=n)
        if cliques:
            return min(sum(clique) for clique in cliques)
    return -1


if __name__ == "__main__":
    print(f"{solution() = }")
