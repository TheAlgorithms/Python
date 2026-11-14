"""
Greedy approximation algorithm for the weighted Set Cover problem.

Given a universe U, a family of subsets of U and a positive cost for each subset,
find a sub-family that covers U with minimum total cost. The problem is NP-hard.

At each step the greedy algorithm picks the subset with the lowest cost per newly
covered element. It is an H(n)-approximation, where n = |U| and
H(n) = 1 + 1/2 + ... + 1/n <= ln(n) + 1 is the n-th harmonic number.

Running time: O(min(m, n) * N), with m subsets of total size N.

https://en.wikipedia.org/wiki/Set_cover_problem#Greedy_algorithm
"""


def greedy_set_cover(
    universe: set[int], subsets: list[set[int]], costs: list[float] | None = None
) -> set[int]:
    """
    Return the indexes of the subsets chosen by the greedy algorithm.

    If no costs are given every subset costs 1, so at each step the algorithm
    picks the subset covering the most uncovered elements.

    >>> greedy_set_cover({1, 2, 3, 4, 5}, [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}])
    {0, 3}

    >>> greedy_set_cover({1, 2, 3, 4}, [{1, 2, 3, 4}, {1, 2}, {3, 4}], [10, 1, 1])
    {1, 2}
    >>> greedy_set_cover({1, 2, 3, 4}, [{1, 2, 3, 4}, {1, 2}, {3, 4}])
    {0}

    >>> greedy_set_cover({1, 2, 3, 4, 5, 6}, [{1, 2, 3, 4}, {1, 2, 5}, {3, 4, 6}])
    {0, 1, 2}

    >>> greedy_set_cover({1, 2}, [{1, 7}, {2, 8}])
    {0, 1}
    >>> greedy_set_cover(set(), [{1, 2}])
    set()

    >>> greedy_set_cover({1, 2, 3}, [{1, 2}, {2}])
    Traceback (most recent call last):
        ...
    ValueError: The given subsets do not cover the universe
    >>> greedy_set_cover({1, 2}, [{1}, {2}], [1.0])
    Traceback (most recent call last):
        ...
    ValueError: Subsets and their costs must have the same length
    >>> greedy_set_cover({1, 2}, [{1}, {2}], [1.0, 0.0])
    Traceback (most recent call last):
        ...
    ValueError: Costs must be positive
    """
    if costs is None:
        costs = [1.0] * len(subsets)
    if len(subsets) != len(costs):
        raise ValueError("Subsets and their costs must have the same length")
    if any(cost <= 0 for cost in costs):
        raise ValueError("Costs must be positive")
    if not universe <= set().union(*subsets):
        raise ValueError("The given subsets do not cover the universe")

    chosen_subsets_indexes: set[int] = set()
    not_chosen_subsets = set(range(len(subsets)))
    elements_to_take = set(universe)
    while elements_to_take:
        # forget the subsets that cover nothing new, so we never divide by 0
        not_chosen_subsets = {
            index for index in not_chosen_subsets if subsets[index] & elements_to_take
        }
        index = min(
            not_chosen_subsets,
            key=lambda index: costs[index] / len(subsets[index] & elements_to_take),
        )
        not_chosen_subsets.remove(index)
        chosen_subsets_indexes.add(index)
        elements_to_take -= subsets[index]

    return chosen_subsets_indexes


if __name__ == "__main__":
    import doctest

    doctest.testmod()
