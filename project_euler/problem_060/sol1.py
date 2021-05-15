"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and
concatenating them in any order the result will always be prime. For example, taking
7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents
the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to
produce another prime.
"""

from itertools import combinations
from math import pow
from typing import Dict, List, TypeVar

PrimeNode = TypeVar("PrimeNode")


def solution(num_of_primes: int = 5) -> int:
    """
    Build a directed graph from every prime number (P) to all of the smaller
    prime numbers (Q) that can be concatenated and form the two following prime
    numbers: PQ and QP.
    For example, if P = 7 we have 3 potential prime numbers for Q: 2, 3, 5.
    - 2 is not a valid neighbor since 27 and 72 are not primes.
    - 3 is a valid neighbor since both 37 and 73 are primes.
    - 5 is not a valid neighbor since 57 and 75 are not primes.
    Therefore, the neighbors of the prime 7 consist of only one prime: 3.

    Once a node has enough neighbors to solve the problem
    (it has >= (num_of_primes - 1) neighbors), we need to check whether these
    neighbors are valid with each other.
    * Why num_of_prime - 1 neighbors is enough: because we need to add the prime
      number P itself as part of the group. We get num_of_primes - 1 neighbors + P,
      which is a group of size num_of_primes.

    - If the neighbors are valid, we found a group of size num_of_primes as required,
      and its sum is the solution.
    - If the neighbors are not valid with each other, continue searching with the next
      prime.

    How do we check if P's neighbors are valid with each other:
    ==========================================================
    We'll tackle it recursively (this is a simplified version
    where the prime P has exactly num_of_primes - 1 neighbors Qs):
    1) Mark the highest neighbor of P to be the new_p and the rest of its
       neighbors set as required_neighbors. Note that the size of the set
       required_neighbors is num_of_primes - 2 (minus the original P and new_p).
    2) If there is a prime number in required_neighbors that isn't a neighbor of
       new_p -> this group is not the solution. Return False.
    3) If all of the prime number in required_neighbors are also neighbors of
       new_p, we repeat step 1.
    4) If the length of required_neighbors is 0 -> It means we were not able to
       negate the group and therefore this is the solution.

    * In case P has more than the exact required size of neighbors (num_of_primes - 1),
      search all the different groups in its neighbors of size (num_of_primes - 1).

    Once finding a group of valid num_of_primes numbers, return its sum.

    >>> solution(3)
    107
    >>> solution(4)
    792
    """
    graph = {}
    all_primes = []
    curr_num = 3
    result = []
    while not result:
        number_to_check = curr_num
        curr_num += 2
        if not is_prime(number_to_check):
            continue
        prime_node = PrimeNode(number_to_check)
        prime_node.populate_neighbors(all_primes, graph)
        all_primes.append(number_to_check)
        graph[number_to_check] = prime_node
        result = search_graph_for_result(graph, num_of_primes - 1, prime_node)
    return sum(result)


class PrimeNode:
    """A basic structure for a prime number node.

    In this problem, neighbors are all the prime numbers that are:
    1) Smaller than the node's value. And -
    2) Create a new prime when concatenating with the node's prime in any order.
    See further explanation and example in the "solution" function above.
    """

    def __init__(self, prime_number: int) -> None:
        """Initialize the node.

        Set the node value to the given prime_number, count its number of
        digits once for future usage and set its neighbors to empty list.
        """
        self.value = prime_number
        self._num_digits = self._calc_num_digits()
        self.neighbors = []

    def _calc_num_digits(self) -> int:
        """Returns the number of digits of the node's value.
        >>> prime_node = PrimeNode(7)
        >>> prime_node._calc_num_digits()
        1
        >>> prime_node = PrimeNode(73)
        >>> prime_node._calc_num_digits()
        2
        >>> prime_node = PrimeNode(7109)
        >>> prime_node._calc_num_digits()
        4
        """
        num_digits = 0
        curr_number = self.value
        while curr_number > 0:
            curr_number //= 10
            num_digits += 1
        return num_digits

    @staticmethod
    def _concat_primes(prime_node_1: PrimeNode, prime_node_2: PrimeNode) -> int:
        """Returns the concatenation of prime_node_1 value and prime_node_2 value as an integer.
        >>> prime_node_1 = PrimeNode(7)
        >>> prime_node_2 = PrimeNode(13)
        >>> PrimeNode._concat_primes(prime_node_1, prime_node_2)
        713
        >>> PrimeNode._concat_primes(prime_node_2, prime_node_1)
        137
        """
        return int(
            pow(10, prime_node_2._num_digits) * prime_node_1.value + prime_node_2.value
        )

    def _is_valid_neighbor(self, other_prime_node: PrimeNode) -> bool:
        """Returns True iff the curr prime node and the other prime node are valid
        neighbors.
        * See definition of valid neighbors in the class doc and solution function.

        >>> prime_node_1 = PrimeNode(109)
        >>> prime_node_2 = PrimeNode(7)
        >>> prime_node_1._is_valid_neighbor(prime_node_2)
        True
        >>> prime_node_1 = PrimeNode(5)
        >>> prime_node_2 = PrimeNode(3)
        >>> prime_node_1._is_valid_neighbor(prime_node_2)
        False
        """
        return is_prime(PrimeNode._concat_primes(self, other_prime_node)) and is_prime(
            PrimeNode._concat_primes(other_prime_node, self)
        )

    def populate_neighbors(
        self, all_smaller_primes: List[int], graph: Dict[int, PrimeNode]
    ) -> None:
        """Search the list of all the primes the are smaller than the node's value
        for valid neighbors.
        * See definition of valid neighbors in the class doc and solution function.

        >>> prime_node = PrimeNode(7)
        >>> all_smaller_primes = [3, 5]
        >>> graph = { 3: PrimeNode(3), 5: PrimeNode(5) }
        >>> prime_node.populate_neighbors(all_smaller_primes, graph)
        >>> prime_node.neighbors
        [3]
        """
        for smaller_prime in all_smaller_primes:
            if self._is_valid_neighbor(graph[smaller_prime]):
                self.neighbors.append(smaller_prime)


def is_prime(number: int) -> bool:
    """Returns True iff number is a prime.

    >>> is_prime(11)
    True
    >>> is_prime(99)
    False
    >>> is_prime(7109)
    True
    >>> is_prime(123456)
    False
    """
    if number <= 2 or number % 2 == 0:
        return number == 2
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True


def validate_prime_set(
    neighbors: List[int], graph: Dict[int, PrimeNode], required_size: int
) -> bool:
    """Returns True iff the given neighbors list is connected in the graph.

    Since the graph connects primes to their valid neighbors, if all the given neighbors
    are connected, it means we have a solution to the problem.
    * See definition of valid neighbors in the solution function doc.

    Suppose we need to find a set of 2 primes (instead of 5 in the problem), and
    we reached to check the prime number 7.
    Its neighbors are [3], and the graph up until now is:
    graph = { 3: PrimeNode(3), 5: PrimeNode(5) } (2 is irrevelant for this problem).
    Also note that we are looking only for one additional prime to get a group of 2
    primes (the priem number 7 and 1 additional prime number):
    >>> neighbors = [3]
    >>> graph = { 3: PrimeNode(3), 5: PrimeNode(5) }
    >>> required_size = 1
    >>> validate_prime_set(neighbors, graph, required_size)
    True

    Suppose we need to find a set of 3 primes (instead of 5 in the problem), and
    we reached to check the prime number 7 as in the previous example.
    Note: we need to find two additional primes (the prime number 7 and two others).
    >>> neighbors = [3]
    >>> graph = { 3: PrimeNode(3), 5: PrimeNode(5) }
    >>> required_size = 2
    >>> validate_prime_set(neighbors, graph, required_size)
    False
    """
    while required_size > 0:
        if not neighbors:
            return False
        curr_prime = neighbors[-1]
        curr_neighbors = neighbors[:-1]
        for prime in curr_neighbors:
            if prime not in graph[curr_prime].neighbors:
                return False
        neighbors = curr_neighbors
        required_size -= 1
    return True


def search_graph_for_result(
    graph: Dict[int, PrimeNode],
    required_number_of_primes: int,
    curr_prime_node: PrimeNode,
) -> List[int]:
    """Returns a list of the primes that solves the question. If there is none in the
    graph, returns an empty list.

    We added a new prime node to the graph, and now we check if this node solves the
    question.
    We'll go over every combination of size required_number_of_primes of its
    neighbors.
    We already know that all of the nodes neighbors are valid comparing to its value,
    we just have to check whether they are valid comparing to each other.

    Suppose we need to find a set of 3 primes (instead of 5 in the problem), and
    we reached to check the prime number 7 as in the previous examples.
    Note: we already have one prime number (7) and looking to add another one:
    >>> graph = { 3: PrimeNode(3), 5: PrimeNode(5) }
    >>> required_number_of_primes = 1
    >>> all_primes = [3, 5]
    >>> curr_prime_node = PrimeNode(7)
    >>> curr_prime_node.populate_neighbors(all_primes, graph)
    >>> search_graph_for_result(graph, required_number_of_primes, curr_prime_node)
    [3, 7]

    Now we'll run the same example but this time with a required set size of 3.
    >>> graph = { 3: PrimeNode(3), 5: PrimeNode(5) }
    >>> required_number_of_primes = 2
    >>> all_primes = [3, 5]
    >>> curr_prime_node = PrimeNode(7)
    >>> curr_prime_node.populate_neighbors(all_primes, graph)
    >>> search_graph_for_result(graph, required_number_of_primes, curr_prime_node)
    []
    """
    if len(curr_prime_node.neighbors) < required_number_of_primes:
        return []
    for comb in combinations(curr_prime_node.neighbors, required_number_of_primes):
        if validate_prime_set(comb, graph, required_number_of_primes):
            return list(comb) + [curr_prime_node.value]
    return []


if __name__ == "__main__":
    print(f"Solution = {solution()}")
