"""
Greedy approximation algorithm for the minimum set cover problem.

Author: Ben Chaddha (https://github.com/benchaddha)

Problem Definition:
    Given a universe U and a collection S of subsets of U such that the union
    of all subsets equals U, find the minimum number of subsets whose union
    covers U.

    This problem is NP-complete (Karp, 1972), making exact solutions
    computationally infeasible for large instances.

Algorithm:
    This implementation uses the standard greedy heuristic that iteratively
    selects the subset covering the most uncovered elements until all elements
    are covered.

Complexity:
    Time: O(|U| * |S|) where |S| is the number of subsets
    Space: O(|U| + |S|)

Approximation Guarantee:
    The greedy algorithm achieves an H_d-approximation where:
    - d = max_i |S_i| (maximum subset size)
    - H_d = sum(1/i for i in 1..d) (d-th harmonic number)
    - H_d ≤ ln(d) + 1

    For the general case, this gives a ln(|U|) + 1 approximation. Feige (1998)
    proved this is essentially optimal: no polynomial-time algorithm can achieve
    a (1 - ε) * ln(|U|) approximation for any ε > 0, unless P = NP.

Limitations:
    - This implementation assumes all subsets have equal cost (unweighted).
    - For the weighted set cover variant, subset selection should be based on
      the cost-effectiveness ratio (uncovered elements / cost).
    - The greedy approach may be far from optimal for specific instances,
      though it provides the theoretical guarantee stated above.

References:
- R. M. Karp, "Reducibility Among Combinatorial Problems", 1972.
- D. S. Johnson, "Approximation algorithms for combinatorial problems", 1974.
- T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein,
  "Introduction to Algorithms", Chapter 35.3, Set Cover.
- U. Feige, "A Threshold of ln n for Approximating Set Cover",
  Journal of the ACM, 45(4), 634-652, 1998.

Note:
    Element and subset identifier types must be hashable for set operations.

Example:
    >>> universe = {1, 2, 3, 4, 5}
    >>> subsets = {
    ...     "A": {1, 2},
    ...     "B": {2, 3, 4},
    ...     "C": {3, 4},
    ...     "D": {4, 5},
    ... }
    >>> cover = greedy_set_cover(universe, subsets)
    >>> # Verify the cover is valid
    >>> set().union(*(subsets[i] for i in cover)) == universe
    True
    >>> # The greedy algorithm selects B and D (or B and a subset covering 1, 5)
    >>> len(cover) <= 3
    True

    >>> # Optimal case: one subset covers everything
    >>> universe2 = {1, 2, 3}
    >>> subsets2 = {"A": {1, 2, 3}, "B": {1}, "C": {2}}
    >>> cover2 = greedy_set_cover(universe2, subsets2)
    >>> cover2 == {"A"}
    True

    >>> # Example showing greedy may not be optimal
    >>> # Optimal is 2 sets {B,C}, but greedy might pick A first
    >>> universe3 = {1, 2, 3, 4}
    >>> subsets3 = {"A": {1, 2}, "B": {1, 3, 4}, "C": {2, 3, 4}}
    >>> cover3 = greedy_set_cover(universe3, subsets3)
    >>> len(cover3) <= 3
    True
    >>> set().union(*(subsets3[i] for i in cover3)) == universe3
    True

    >>> # Error handling - empty universe
    >>> greedy_set_cover(set(), {"A": {1}})
    Traceback (most recent call last):
        ...
    ValueError: Universe must be non-empty.

    >>> # Error handling - empty subsets
    >>> greedy_set_cover({1, 2}, {})
    Traceback (most recent call last):
        ...
    ValueError: Subsets mapping must be non-empty.

    >>> # Error handling - subsets don't cover universe
    >>> greedy_set_cover({1, 2, 3}, {"A": {1}, "B": {2}})
    Traceback (most recent call last):
        ...
    ValueError: The provided subsets do not cover the universe.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping


def greedy_set_cover(
    universe: Iterable[Hashable],
    subsets: Mapping[Hashable, Iterable[Hashable]],
) -> set[Hashable]:
    """
    Greedy approximation for minimum set cover.

    Args:
        universe: The set of elements to be covered.
        subsets: A mapping from subset identifiers to their elements.

    Returns:
        A set of subset identifiers that covers the universe.

    Raises:
        ValueError: If the universe is empty, subsets is empty, or if the
                   provided subsets cannot cover the universe.

    Time Complexity: O(|universe| * |subsets|)
    Space Complexity: O(|universe| + |subsets|)
    """

    # Normalize inputs to sets so we do not mutate user-provided structures.
    universe_set = set(universe)
    if not universe_set:
        raise ValueError("Universe must be non-empty.")

    if not subsets:
        raise ValueError("Subsets mapping must be non-empty.")

    normalized_subsets: dict[Hashable, set[Hashable]] = {
        key: set(s) for key, s in subsets.items()
    }

    # Quick feasibility check: if the union of all subsets does not cover U,
    # we can terminate early. This is preferable to silently returning
    # an incomplete "cover".
    union_of_subsets: set[Hashable] = set().union(*normalized_subsets.values())
    if not universe_set.issubset(union_of_subsets):
        raise ValueError("The provided subsets do not cover the universe.")

    uncovered: set[Hashable] = set(universe_set)
    chosen_subsets: set[Hashable] = set()

    # Standard greedy loop: at each step, select the subset that covers
    # the largest number of remaining uncovered elements.
    while uncovered:
        best_key: Hashable | None = None
        best_gain = 0

        for key, subset in normalized_subsets.items():
            if key in chosen_subsets:
                continue  # already selected
            # Intersection with uncovered elements gives the marginal gain.
            gain = len(uncovered & subset)
            if gain > best_gain:
                best_gain = gain
                best_key = key

        # If no subset yields a positive gain, but uncovered is non-empty,
        # the instance is effectively uncoverable (should not happen if the
        # feasibility check above passed, but we keep this for robustness).
        if best_key is None or best_gain == 0:
            raise ValueError("The provided subsets do not cover the universe.")

        # Commit to the chosen subset and mark its elements as covered.
        chosen_subsets.add(best_key)
        uncovered -= normalized_subsets[best_key]

    return chosen_subsets


if __name__ == "__main__":
    import doctest

    doctest.testmod()
