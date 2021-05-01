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
    Build a dirrected graph from every primes to all the smaller primes
    such that every neighbor of a prime is creates two primes by concatenating
    it to the node's value.

    Whenever a node has enough neighbors to solve the problem, check if all
    the neighbors are valid with each other -
    1) Iterate on the node's neighbors from the highest primes to the lowest
    2) Make sure all the lower primes appear in the prime's node as neighbors.

    Once you find a node that has num_of_primes valid neighbors and they are
    valid with each other, return the sum of all the relevant primes.

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
    """A basic structure for a prime number and all of its neighbors.

    In this problem, neighbors are all the primes that:
    1) Smaller than the node's prime. And -
    2) Create a new prime when concatenating with the node's prime in any order.

    Example: if the node's value is 7, its neighbors will be [3]. Because all the primes
    the are smaller than 7 are: 2, 3, 5. But 3 is the only prime number that can be
    concatenated to 7 in any order and will create primes: 37 & 73.
    """

    def __init__(self, prime_number: int) -> None:
        """Initialize the node.

        Set the prime number's value to the given prime_number, count its number of
        digits once and set its neighbors to empty list.
        """
        self.value = prime_number
        self.num_digits = self._calc_num_digits()
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
            pow(10, prime_node_2.num_digits) * prime_node_1.value + prime_node_2.value
        )

    def _is_valid_neighbor(self, other_prime_node: PrimeNode) -> bool:
        """Returns True iff the curr prime node and the other prime node are valid
        neighbors.
        * See definition of valid neighbors in the class doc.

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
        """Search the list of all the primes the are smaller than the node's prime
        for valid neighbors.
        * See definition of valid neighbors in the class doc.

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
    * See definition of valid neighbors in the class doc.

    Suppose we need to find a set of 2 primes (instead of 5 in the problem). Looking at
    the prime_node of 7, we already have 1 prime and looking to add another 1:
    >>> neighbors = [3]
    >>> graph = { 3: PrimeNode(3), 5: PrimeNode(5) }
    >>> required_size = 1
    >>> validate_prime_set(neighbors, graph, required_size)
    True

    Suppose we need to find a set of 3 primes (instead of 5 in the problem). Looking at
    the prime_node of 7, we already have 1 prime and looking to add another 2:
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

    Suppose we need to find a set of 2 primes (instead of 5 in the problem). Looking at
    the prime_node of 7, we already have 1 prime and looking to add another 1:
    >>> graph = { 3: PrimeNode(3), 5: PrimeNode(5) }
    >>> required_number_of_primes = 1
    >>> all_primes = [3, 5]
    >>> curr_prime_node = PrimeNode(7)
    >>> curr_prime_node.populate_neighbors(all_primes, graph)
    >>> search_graph_for_result(graph, required_number_of_primes, curr_prime_node)
    [3, 7]

    Suppose we need to find a set of 3 primes (instead of 5 in the problem). Looking at
    the prime_node of 7, we already have 1 prime and looking to add another 2:
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
