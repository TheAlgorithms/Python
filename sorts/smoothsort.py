"""
Smoothsort algorithm implementation.

Smoothsort is an adaptive, in-place comparison sort invented by Edsger W. Dijkstra.
It runs in O(n log n) worst-case and degrades gracefully to O(n) for nearly sorted data.
It uses a forest of Leonardo heaps to achieve this adaptive behaviour.

Reference:
    https://en.wikipedia.org/wiki/Smoothsort
    https://www.cs.utexas.edu/~EWD/ewd07xx/EWD796a.PDF
"""


# Precomputed Leonardo numbers: L(0)=1, L(1)=1, L(k)=L(k-1)+L(k-2)+1.
# 46 values comfortably cover all practical list sizes.
_LEONARDO: list[int] = [1, 1]
while _LEONARDO[-1] < 2**31:
    _LEONARDO.append(_LEONARDO[-1] + _LEONARDO[-2] + 1)


def _sift(seq: list[int], root: int, order: int) -> None:
    """
    Restore the max-heap property within a Leonardo tree of the given ``order``.

    Sifts ``seq[root]`` downward until the subtree satisfies the Leonardo
    max-heap invariant: every node is >= both of its children.
    Trees of order 0 or 1 are single nodes and already satisfy the invariant.

    In a Leonardo tree of order k rooted at index ``root``:
      - the right child root is at ``root - 1``
      - the left  child root is at ``root - 1 - L(k-2)``

    Args:
        seq:   The list being sorted (mutated in-place).
        root:  Index of the root of the Leonardo tree to fix.
        order: Leonardo order of the tree rooted at ``root``.

    Examples:
        >>> data = [3, 5, 4]
        >>> _sift(data, 2, 2)
        >>> data
        [3, 4, 5]

        >>> data = [1, 2, 3]
        >>> _sift(data, 2, 2)
        >>> data
        [1, 2, 3]

        >>> data = [7]
        >>> _sift(data, 0, 1)
        >>> data
        [7]

        >>> data = [9, 1, 8, 5, 3]
        >>> _sift(data, 4, 3)
        >>> data
        [3, 1, 9, 5, 8]
    """
    while order > 1:
        right = root - 1                             # right child root
        left = root - 1 - _LEONARDO[order - 2]      # left child root

        if seq[left] >= seq[right] and seq[left] > seq[root]:
            seq[root], seq[left] = seq[left], seq[root]
            root = left
            order -= 1
        elif seq[right] > seq[left] and seq[right] > seq[root]:
            seq[root], seq[right] = seq[right], seq[root]
            root = right
            order -= 2
        else:
            break


def _trinkle(
    seq: list[int],
    pos: int,
    heap_sizes: list[int],
    idx: int,
) -> None:
    """
    Restore both the inter-heap root ordering and the intra-heap ordering.

    Walks the value at ``pos`` leftwards through the forest-root chain as
    long as the left-neighbour root is larger, then calls ``_sift`` to fix
    the heap at the final resting position.

    Args:
        seq:        The list being sorted (mutated in-place).
        pos:        Index of the root being inserted or newly exposed.
        heap_sizes: List of Leonardo orders for the current forest (left to
                    right); ``heap_sizes[idx]`` is the order of the tree
                    whose root is at ``pos``.
        idx:        Position in ``heap_sizes`` for the tree rooted at ``pos``.

    Examples:
        >>> data = [1, 5, 3]
        >>> _trinkle(data, 2, [1, 1], 1)
        >>> data
        [1, 3, 5]

        >>> data = [3, 5, 4]
        >>> _trinkle(data, 2, [2], 0)
        >>> data
        [3, 4, 5]
    """
    while idx > 0:
        prev_root = pos - _LEONARDO[heap_sizes[idx]]
        if seq[pos] >= seq[prev_root]:
            break
        # Only swap if prev_root is also >= its own children; otherwise
        # moving it would break the heap on the left side.
        if heap_sizes[idx] > 1:
            right = pos - 1
            left = pos - 1 - _LEONARDO[heap_sizes[idx] - 2]
            if seq[prev_root] <= seq[right] or seq[prev_root] <= seq[left]:
                break
        seq[pos], seq[prev_root] = seq[prev_root], seq[pos]
        pos = prev_root
        idx -= 1

    _sift(seq, pos, heap_sizes[idx])


def smoothsort(seq: list[int]) -> list[int]:
    """
    Sort a list in-place using the Smoothsort algorithm and return it.

    Smoothsort (Edsger W. Dijkstra, 1981) is an adaptive, in-place sort
    with O(n log n) worst-case time and O(n) best-case time on already-sorted
    input.  It improves on Heapsort by maintaining a forest of Leonardo heaps
    whose structure mirrors the sorted prefix of the sequence.

    Args:
        seq: A list of integers to sort.

    Returns:
        The same list object, sorted in ascending order.

    Examples:
        >>> smoothsort([4, 1, 3, 9, 7])
        [1, 3, 4, 7, 9]
        >>> smoothsort([])
        []
        >>> smoothsort([1])
        [1]
        >>> smoothsort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
        >>> smoothsort([3, 3, 2, 1, 2])
        [1, 2, 2, 3, 3]
        >>> smoothsort([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> smoothsort([-3, 0, -1, 5, 2])
        [-3, -1, 0, 2, 5]
    """
    n = len(seq)
    if n < 2:
        return seq

    # ``heap_sizes[i]`` is the Leonardo order of the i-th tree (left to right).
    heap_sizes: list[int] = []

    # ------------------------------------------------------------------
    # Phase 1 – Build the Leonardo heap forest over seq[0..n-1].
    # ------------------------------------------------------------------
    for i in range(n):
        # If the two rightmost trees have consecutive orders, merge them.
        if (
            len(heap_sizes) >= 2
            and heap_sizes[-2] == heap_sizes[-1] + 1
        ):
            heap_sizes.pop()
            heap_sizes[-1] += 1
        elif heap_sizes and heap_sizes[-1] == 1:
            heap_sizes.append(0)
        else:
            heap_sizes.append(1)

        _trinkle(seq, i, heap_sizes, len(heap_sizes) - 1)

    # ------------------------------------------------------------------
    # Phase 2 – Extract maximum elements right-to-left.
    # ------------------------------------------------------------------
    for i in range(n - 1, -1, -1):
        order = heap_sizes.pop()
        if order > 1:
            # Expose the two child roots and re-trinkle each.
            right_order = order - 2
            left_order = order - 1
            right_pos = i - 1
            left_pos = i - 1 - _LEONARDO[right_order]

            heap_sizes.append(left_order)
            _trinkle(seq, left_pos, heap_sizes, len(heap_sizes) - 1)

            heap_sizes.append(right_order)
            _trinkle(seq, right_pos, heap_sizes, len(heap_sizes) - 1)

    return seq


if __name__ == "__main__":
    import doctest
    import random

    results = doctest.testmod(verbose=False)
    assert results.failed == 0, f"{results.failed} doctest(s) failed"

    for trial in range(5000):
        sample = random.choices(range(-50, 50), k=random.randint(0, 30))
        got = smoothsort(sample[:])
        assert got == sorted(sample), (
            f"Trial {trial}: smoothsort({sample!r}) -> {got!r}, "
            f"expected {sorted(sample)!r}"
        )

    print("All doctests and 5 000 random trials passed.")
