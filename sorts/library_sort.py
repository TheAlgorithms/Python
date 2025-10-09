"""
Library Sort (Gapped Insertion) — Enhanced and Documented

Concept:
- Library Sort is a gapped version of insertion sort that keeps extra empty
  slots between placed elements, so most insertions do not require shifting
  a long suffix of the array. The algorithm occasionally "rebalances" the
  layout to redistribute elements and restore evenly spaced gaps. This yields
  an expected average complexity of O(n log n) under typical (non-adversarial)
  input distributions.

API:
- library_sort(data, key=None, reverse=False, epsilon=1.0) -> List
  - data: any iterable of items
  - key: optional key extractor like built-in sorted()/list.sort()
  - reverse: set True for descending order
  - epsilon: extra-space factor controlling how many gaps are left in the
             backing array (larger epsilon = more gaps = fewer collisions,
             more memory)

Complexity (informal):
- Average (with high probability): O(n log n) thanks to binary search for the
  logical order plus amortized O(1) gap insertions.
- Worst case: O(n^2) if inputs are adversarial and repeatedly force dense
  regions, even after rebalancing.
- Space: O(n * (1 + epsilon)) for the gapped array.

Notes for learners:
- We maintain two parallel arrays:
  - A_keys: holds keys in a sparse (gapped) physical layout.
  - A_vals: holds the original values at the same indices as A_keys.
- We also maintain a 'pos' list that records the indices of the FILLED
  positions in sorted, logical order. This lets us:
  (1) binary-search the correct logical position for a new key
  (2) ask for a "desired physical slot" roughly midway between neighbors
      so we’re likely to find (or make) a gap near that logical position.
- If there is no gap at the desired slot, we "rebalance" by redistributing
  the existing items farther apart, restoring even gaps before retrying.

This annotated implementation focuses on clarity and pedagogy rather than
micro-optimizations, so readers can trace each step of the algorithm.
"""

from typing import Callable, Iterable, List, Optional, Tuple
import bisect


def library_sort(
    data: Iterable,
    key: Optional[Callable] = None,
    reverse: bool = False,
    epsilon: float = 1.0,
) -> List:
    """
    Sort 'data' using Library Sort (gapped insertion) and return a new list.

    Parameters
    ----------
    data : Iterable
        Items to sort.
    key : Callable | None
        Optional key extractor (like built-in sorted()).
    reverse : bool
        If True, return results in descending order.
    epsilon : float
        Extra-space factor controlling gap density; larger values create
        more gaps, which reduces collisions but uses more memory.

    Returns
    -------
    List
        A new list containing the sorted items.

    Teaching tip:
    - Think of 'pos' as the logical, in-order view (where elements "should"
      be if there were no gaps), and 'A_keys/A_vals' as the physical shelves
      that include empty spots to make insertions cheap.
    """
    # Materialize input and handle trivial sizes.
    items = list(data)
    n = len(items)
    if n < 2:
        return items.copy()

    # Normalize to a key/value representation so we can sort arbitrary objects.
    key_fn = key if key is not None else (lambda x: x)
    keyed: List[Tuple] = [(key_fn(x), x) for x in items]

    # Capacity with slack: leave about 'epsilon' * n empty slots as gaps.
    # The +1 ensures at least one spare slot even for small inputs.
    cap = max(3, int((1.0 + epsilon) * n) + 1)

    # Sparse physical storage for keys/values; None marks a gap (empty slot).
    A_keys: List[Optional[Tuple]] = [None] * cap
    A_vals: List[Optional[object]] = [None] * cap

    # 'pos' tracks indices of FILLED slots in sorted order of keys.
    # This lets us binary-search by logical rank, independent of gaps.
    pos: List[int] = []

    # Seed the structure by placing the first element near the middle so
    # we can grow to both sides without immediate rebalancing.
    mid = cap // 2
    A_keys[mid] = keyed[0][0]
    A_vals[mid] = keyed[0][1]
    pos.append(mid)

    def rebalance(target_count: int) -> None:
        """
        Redistribute elements with fresh gaps.

        Given we currently have 'target_count' filled items, rebuild 'pos'
        into a new array of size ≈ (1 + epsilon) * target_count, spacing
        items roughly evenly so subsequent insertions are likely to find
        nearby gaps.
        """
        nonlocal A_keys, A_vals, pos, cap

        # Grow capacity if needed to preserve slack proportional to item count.
        cap = max(cap, int((1.0 + epsilon) * target_count) + 3)

        # Compute a stride so that (target_count) items are spaced out with gaps.
        step = max(1, cap // (target_count + 1))
        start = step // 2  # small offset so ends aren't packed

        new_keys: List[Optional[Tuple]] = [None] * cap
        new_vals: List[Optional[object]] = [None] * cap
        new_pos: List[int] = []

        # Copy each existing filled slot to its new, spaced-out location.
        for i, old_idx in enumerate(pos):
            new_index = start + i * step
            new_keys[new_index] = A_keys[old_idx]
            new_vals[new_index] = A_vals[old_idx]
            new_pos.append(new_index)

        A_keys, A_vals, pos = new_keys, new_vals, new_pos

    def desired_slot(rank: int) -> int:
        """
        Given the logical insertion rank (the index where the new key would go
        in sorted order), return a physical index that lies between its neighbors.

        This heuristic aims for the midpoint between adjacent filled indices
        to maximize the chance we land on, or near, a gap.
        """
        if rank == 0:
            return pos[0] - 1  # just before first filled slot
        if rank == len(pos):
            return pos[-1] + 1  # just after last filled slot
        return (pos[rank - 1] + pos[rank]) // 2  # midpoint between neighbors

    # Insert remaining items one by one.
    for k, v in keyed[1:]:
        # Binary-search the logical order of existing keys using 'pos'.
        logical_keys = [A_keys[i] for i in pos]
        ins_rank = bisect.bisect_left(logical_keys, k)

        tries = 0
        while True:
            # Ask for a good physical slot near the desired rank.
            idx = desired_slot(ins_rank)

            # If it's a valid gap, claim it and record the new filled position.
            if 0 <= idx < cap and A_keys[idx] is None:
                A_keys[idx] = k
                A_vals[idx] = v
                pos.insert(ins_rank, idx)
                break

            # Otherwise, things are too dense around there; rebalance to
            # re-open gaps and try again.
            tries += 1
            rebalance(len(pos) + 1)

            # Safety valve: if local density remains high after a few passes,
            # gradually increase epsilon (more gaps) and rebalance again.
            if tries > 3:
                epsilon *= 1.25
                rebalance(len(pos) + 1)
                tries = 0

    # Stitch the final, in-order values back together using 'pos'.
    out = [A_vals[i] for i in pos]  # type: ignore
    if reverse:
        out.reverse()
    return out


if __name__ == "__main__":
    # Minimal demo to visualize behavior.
    data = [34, 7, 23, 32, 5, 62, 14, 19, 45, 38]
    print("Before:", data)
    print("After: ", library_sort(data))
