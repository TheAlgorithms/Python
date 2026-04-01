"""Progressive multi-set intersection optimized for imbalanced sets."""

from typing import Set


def progressive_set_intersection(*sets: Set) -> Set:
    """
    Compute the intersection of multiple sets efficiently.

    This function sorts the input sets by size (smallest first) and
    progressively intersects them. It includes early termination when
    the result becomes empty, which is very effective when dealing with
    many sets or highly imbalanced sizes (e.g., one small set + many large ones).

    Python's built-in `set.intersection(*sets)` is already optimized in C,
    but this implementation demonstrates the "smallest-first + prune early"
    heuristic for educational purposes.

    Time Complexity: Better than naive in practice due to early pruning.

    Examples:
        >>> progressive_set_intersection({1, 2, 3}, {2, 3, 4}, {2, 5})
        {2}
        >>> progressive_set_intersection({1, 2}, {3, 4})
        set()
        >>> progressive_set_intersection({10, 20, 30})
        {10, 20, 30}
        >>> progressive_set_intersection()
        set()
    """
    if not sets:
        return set()

    if len(sets) == 1:
        return sets[0].copy()

    # Sort by length (smallest first) for optimal pruning
    sorted_sets = sorted(sets, key=len)

    result = sorted_sets[0].copy()

    for current_set in sorted_sets[1:]:
        if not result:
            return set()
        result &= current_set   # Efficient in-place intersection

    return result
